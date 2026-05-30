from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers

from posts.models.hashtag import Hashtag
from posts.serializers.hashtag import HashtagSerializer
from posts.models.posts import Post
from core.services.extend_actions import ExtendActions


class HashtagViewSet(ExtendActions, ModelViewSet):
    serializer_class = HashtagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Hashtag.objects.all()