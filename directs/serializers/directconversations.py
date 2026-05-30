from django.db import transaction
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from directs.models.directconversations import DirectConversation
from directs.serializers.directmessage import ChatUserSerializer

User = get_user_model()

class DirectConversationSerializer(serializers.ModelSerializer):
    user = ChatUserSerializer(many=True, read_only=True)

    class Meta:
        model = DirectConversation
        fields = ("id", "user", "created_at")


class DirectConversationCreateSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(
        many=True, queryset=User.objects.all(), source='user'
    )

    class Meta:
        model = DirectConversation
        fields = ["users"]

    def validate(self, attrs):
        users = attrs.get('user', [])
        current_user = self.context['request'].user

        if current_user in users:
            raise ValidationError({"users": "You cannot add yourself to the conversation."})

        if not users:
            raise ValidationError({"users": "At least one other user is required."})

        return attrs

    def create(self, validated_data):
        current_user = self.context['request'].user
        other_users = validated_data['user']
        
       
        if len(other_users) == 1:
            target_user = other_users[0]
            existing_conv = DirectConversation.objects.filter(
                user=current_user
            ).filter(user=target_user).first()
            
            if existing_conv:
                return existing_conv

        with transaction.atomic():
            conversation = DirectConversation.objects.create()
            conversation.user.add(current_user, *other_users)
            return conversation
