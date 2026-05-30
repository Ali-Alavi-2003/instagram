from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from directs.models.directmessage import DirectMessage

User = get_user_model()


class ChatUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class DirectMessageSerializer(serializers.ModelSerializer):
    sender = ChatUserSerializer(read_only=True)
    conversation = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = DirectMessage
        fields = [
            "id",
            "conversation",
            "sender",
            "message",
            "file",
            "created_at",
        ]
        read_only_fields = ["sender", "conversation"]


class DirectMessageCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = DirectMessage
        fields = ["message", "file"]

    def validate(self, attrs):
        message = attrs.get("message")
        file = attrs.get("file")

        if not message and not file:
            raise ValidationError("Message cannot be empty. Provide text or a file.")

        return attrs

    def create(self, validated_data):
        request = self.context["request"]
        conversation = self.context["conversation"]

        if request.user not in conversation.user.all():
            raise ValidationError("You are not a member of this conversation.")

        with transaction.atomic():
            msg = DirectMessage.objects.create(
                sender=request.user,
                conversation=conversation,
                **validated_data
            )
            return msg
