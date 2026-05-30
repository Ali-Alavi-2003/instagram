from rest_framework import serializers
from .models import Follow


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = [
            "id",
            "follower",
            "following",
            "created_at",
        ]
        read_only_fields = ["id", "follower", "created_at"]

class FollowCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ["following"]

    def validate_following(self, value):
        request = self.context["request"]

        if request.user == value:
            raise serializers.ValidationError("You cannot follow yourself.")

        if Follow.objects.filter(
            follower=request.user,
            following=value
        ).exists():
            raise serializers.ValidationError("You already follow this user.")

        return value

    def create(self, validated_data):
        return Follow.objects.create(
            follower=self.context["request"].user,
            **validated_data
        )
