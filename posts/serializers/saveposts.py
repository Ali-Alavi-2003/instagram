from rest_framework import serializers

from posts.models.saveposts import SavePost
from posts.models.posts import Post
from posts.serializers.posts import PostSerializer


class SavePostReadSerializer(serializers.ModelSerializer):
    post = PostSerializer(read_only=True)

    class Meta:
        model = SavePost
        fields = ('id', 'post')


class SavePostCreateSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all()
    )

    class Meta:
        model = SavePost
        fields = ('id', 'post')
