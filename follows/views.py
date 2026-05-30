from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Follow
from .serializers import FollowSerializer, FollowCreateSerializer


class FollowViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "delete"]

    def get_queryset(self):
        return (
            Follow.objects
            .filter(follower=self.request.user)
            .select_related("follower", "following")
            .order_by("-created_at")
        )

    def get_serializer_class(self):
        if self.action in ("create", "toggle"):
            return FollowCreateSerializer
        return FollowSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        follow = serializer.save()

        out = FollowSerializer(follow, context=self.get_serializer_context())
        return Response(out.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=["get"], url_path="followers")
    def followers(self, request):
        queryset = (
            Follow.objects
            .filter(following=request.user)
            .select_related("follower", "following")
            .order_by("-created_at")
        )

        serializer = FollowSerializer(
            queryset, many=True, context=self.get_serializer_context()
        )
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"], url_path="followings")
    def followings(self, request):
        queryset = (
            Follow.objects
            .filter(follower=request.user)
            .select_related("follower", "following")
            .order_by("-created_at")
        )

        serializer = FollowSerializer(
            queryset, many=True, context=self.get_serializer_context()
        )
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"], url_path="status")
    def status(self, request):
        user_id = request.query_params.get("user")
        if not user_id:
            return Response(
                {"detail": "user query param is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        obj = Follow.objects.filter(
            follower=request.user,
            following_id=user_id,
        ).only("id").first()

        return Response(
            {"is_following": obj is not None, "follow_id": obj.id if obj else None},
            status=status.HTTP_200_OK,
        )

    @action(detail=False, methods=["post"], url_path="toggle")
    def toggle(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        following_user = serializer.validated_data["following"]

        obj = Follow.objects.filter(
            follower=request.user,
            following=following_user,
        ).first()

        if obj:
            obj.delete()
            return Response(
                {"detail": "Unfollowed successfully.", "is_following": False},
                status=status.HTTP_200_OK,
            )

        follow = Follow.objects.create(
            follower=request.user,
            following=following_user,
        )

        out = FollowSerializer(follow, context=self.get_serializer_context()).data
        out["is_following"] = True
        return Response(out, status=status.HTTP_201_CREATED)
