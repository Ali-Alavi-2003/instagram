# from rest_framework.serializers import ModelSerializer

# from django.contrib.auth import get_user_model
# from posts.models.likes import Like
# from posts.models.posts import Post
# from posts.serializers.posts import RetrievePostSerializer
# from accounts.serializer.authuser import UserSerializer

# User = get_user_model()

# class LikeSerializer(ModelSerializer):
#     class Meta:
#         model = Like
#         fields = ['id', 'user', 'post']
#         read_only_fields = ['id', 'user']

#     def create(self, validated_data):
#         request = self.context.get('request')
#         user = request.user
#         post = validated_data['post']
#         like, created = Like.objects.get_or_create(user=user, post=post)
#         return like