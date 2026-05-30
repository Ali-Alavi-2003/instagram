from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from posts.models.comments import Comment
from accounts.serializer.authuser import UserSerializer



class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields= (
            'id',
            'user',
            'post',
            'text',
            'comment',
            'created_at',
        )
        read_only_fields = ['id','user', 'created_at']
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    

class ReplySerializer(ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'text',
            'created_at',
        )


class CommentDetailSerializer(ModelSerializer):
    user = serializers.StringRelatedField()
    replies = ReplySerializer(many=True, source='reply', read_only=True)

    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'text',
            'created_at',
            'replies'
        ]
