from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from posts.models.comments import Comment
from posts.serializers.comments import CommentSerializer
from posts.serializers.comments import CommentDetailSerializer

class CommentModelViewset(ModelViewSet):
    permission_classes =[IsAuthenticated]
    def get_queryset(self):
        return Comment.objects.select_related('user', 'post', 'comment').prefetch_related('reply')
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CommentDetailSerializer
        return CommentSerializer
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)