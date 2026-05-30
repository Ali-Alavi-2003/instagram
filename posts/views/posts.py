from rest_framework.viewsets import ModelViewSet
from posts.serializers.posts import PostSerializer, RetrievePostSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema
from django.db.models import Count, Exists, OuterRef, Value, BooleanField
from rest_framework.response import Response
from rest_framework import status


from core.services.extend_actions import ExtendActions
from posts.models.likes import Like
from posts.models.posts import Post

class PostViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]

    # queryset = Post.objects.all()
    serializer_class = PostSerializer

    filter_backends = [SearchFilter]
    search_fields = ['hashtags__body']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
    
    def get_queryset(self):
        return Post.objects.filter(user = self.request.user).prefetch_related('hashtags')
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class AllPostViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'patch', 'put', 'delete', 'head', 'options']

    def get_queryset(self):
        user = self.request.user
        
        queryset = Post.objects.select_related('user').prefetch_related(
            'comments',
            'comments__user',
            'comments__reply',
            'comments__reply__user',
        )

        queryset = queryset.annotate(like_count_val=Count('likes', distinct=True))

        if user.is_authenticated:
            queryset = queryset.annotate(
                is_liked_val=Exists(
                    Like.objects.filter(post=OuterRef('pk'), user=user)
                )
            )
        else:
            queryset = queryset.annotate(
                is_liked_val=Value(False, output_field=BooleanField())
            )

        return queryset.order_by('-created_at')

    def get_serializer_class(self):
        if self.action == 'list':
            return PostSerializer
        return RetrievePostSerializer

    @extend_schema(exclude=True)
    def create(self, request, *args, **kwargs):
        return Response(
            {'detail': 'This endpoint is disabled'},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user

        like_obj, created = Like.objects.get_or_create(user=user, post=post)

        if not created:
            like_obj.delete()
            return Response(
                {'detail': 'unliked', 'like_count': post.likes.count()},
                status=status.HTTP_200_OK
            )

        return Response(
            {'detail': 'liked', 'like_count': post.likes.count()},
            status=status.HTTP_201_CREATED
        )
