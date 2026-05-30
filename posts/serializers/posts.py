from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

from posts.models.posts import Post
from posts.services.extraction_hashtag import ExtractionHashtag
from accounts.serializer.authuser import UserSerializer
from posts.models.likes import Like
from posts.serializers.comments import CommentDetailSerializer


User = get_user_model()

class PostSerializer(ModelSerializer):
    username = serializers.ReadOnlyField(source='user.phone_number')
    user_avatar = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    img = serializers.ImageField(required=False)
    comments = CommentDetailSerializer(many = True, read_only = True)

    class Meta:
        model = Post
        fields = [
            'id',
            'username',
            'user_avatar',
            'img',
            'caption',
            'comments',
            'is_liked',
            'like_count',
        ]
    
    def get_user_avatar(self, obj):
        try:
            if obj.user.profile.avatar:
                request = self.context.get('request')
                return request.build_absolute_uri(obj.user.profile.avatar.url)
        except:
            return None
        return None

    def get_is_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(user=request.user).exists()
        return False

    def create(self, validated_data):
        post = super().create(validated_data)
        ExtractionHashtag.extract(post)
        return post

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        ExtractionHashtag.extract(instance)
        return instance


    
class RetrievePostSerializer(ModelSerializer):
    like_count = serializers.IntegerField(source='like_count_val', read_only=True)
    is_liked = serializers.BooleanField(source='is_liked_val', read_only=True)
    comments = CommentDetailSerializer(many = True, read_only = True)
    user_phone = serializers.CharField(source='user.phone_number', read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'user_phone',
            'img',
            'caption',
            'comments',
            'like_count',
            'is_liked',
        ]
        read_only_fields = ['id', 'user', 'like_count', 'is_liked', 'comments']
    # def create(self, validated_data):
    #     request = self.context.get('request')
    #     user = request.user
    #     return Post.objects.create(user=user, **validated_data)
    
    # def get_is_liked(self, obj):
    #     request = self.context.get('request')
    #     if not request or not request.user.is_authenticated:
    #         return False
    #     return Like.objects.filter(post=obj, user=request.user).exists()