from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

from accounts.models.profile import Profile
from posts.serializers.posts import PostSerializer
from accounts.serializer.authuser import UserSerializer

from follows.models import Follow 

User = get_user_model()


class ProfileSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    phone_number = serializers.ReadOnlyField(source="user.phone_number")

    posts = PostSerializer(source="user.posts", many=True, read_only=True)
    posts_count = serializers.IntegerField(source="user.posts.count", read_only=True)

    followers_count = serializers.IntegerField(source="user.follower.count", read_only=True)
    following_count = serializers.IntegerField(source="user.following.count", read_only=True)

    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
            "phone_number",
            "avatar",
            "bio",
            "is_private",
            "is_active",
            "posts",
            "posts_count",
            "followers_count",
            "following_count",
        )

    def update(self, instance, validated_data):
        user_data = self.context["request"].data.get("user")

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if user_data and isinstance(user_data, dict):
            user_instance = instance.user
            for attr, value in user_data.items():
                setattr(user_instance, attr, value)
            user_instance.save()

        return instance
