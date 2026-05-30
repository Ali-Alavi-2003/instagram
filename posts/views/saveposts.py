from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from posts.models.saveposts import SavePost
from posts.serializers.saveposts import (
    SavePostReadSerializer,
    SavePostCreateSerializer,
)


class SavePostViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SavePost.objects.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        if self.action == 'create':
            return SavePostCreateSerializer
        return SavePostReadSerializer

    def create(self, request, *args, **kwargs):
        post_id = request.data.get('post')

        if not post_id:
            return Response(
                {"post": ["This field is required."]},
                status=status.HTTP_400_BAD_REQUEST
            )

        if SavePost.objects.filter(user=request.user, post_id=post_id).exists():
            return Response(
                {"detail": "قبلاً ذخیره شده"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        read_serializer = SavePostReadSerializer(
            serializer.instance,
            context={'request': request}
        )
        return Response(read_serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
