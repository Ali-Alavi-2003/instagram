from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from django.shortcuts import get_object_or_404

from directs.models import DirectConversation, DirectMessage
from directs.serializers import (
    DirectConversationSerializer,
    DirectConversationCreateSerializer,
    DirectMessageSerializer,
    DirectMessageCreateSerializer,
)


class IsConversationMember(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        return request.user in obj.user.all()


class DirectConversationViewSet(ModelViewSet):

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (
            DirectConversation.objects.filter(user=self.request.user)
            .prefetch_related("user")
            .order_by("-created_at")
        )

    def get_serializer_class(self):
        return (
            DirectConversationCreateSerializer
            if self.action == "create"
            else DirectConversationSerializer
        )

    @action(detail=True, methods=["get"], permission_classes=[IsConversationMember])
    def messages(self, request, pk=None):
        conversation = self.get_object()

        qs = DirectMessage.objects.filter(
            conversation=conversation
        ).select_related("sender").order_by("id")

        serializer = DirectMessageSerializer(
            qs, many=True, context=self.get_serializer_context()
        )
        return Response(serializer.data)


    @action(detail=True, methods=["post"], permission_classes=[IsConversationMember])
    def send_message(self, request, pk=None):
        conversation = self.get_object()

        serializer = DirectMessageCreateSerializer(
            data=request.data,
            context={**self.get_serializer_context(), "conversation": conversation},
        )
        serializer.is_valid(raise_exception=True)
        message = serializer.save()

        out = DirectMessageSerializer(message, context=self.get_serializer_context())
        return Response(out.data, status=status.HTTP_201_CREATED)


class DirectMessageViewSet(ModelViewSet):

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (
            DirectMessage.objects.filter(conversation__user=self.request.user)
            .select_related("sender", "conversation")
            .order_by("-created_at")
        )

    def get_serializer_class(self):
        return (
            DirectMessageCreateSerializer
            if self.action == "create"
            else DirectMessageSerializer
        )

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
