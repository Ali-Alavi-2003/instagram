from rest_framework import serializers
from .models import Story
from accounts.serializer.authuser import UserSerializer

class StorySerializer(serializers.ModelSerializer):
    user_details = UserSerializer(source='user', read_only=True)

    class Meta:
        model = Story
        fields = [
            "id",
            "user",
            "user_details",
            "img",
            "created_at",
        ]
        read_only_fields = ('id', 'user', 'created_at',)
