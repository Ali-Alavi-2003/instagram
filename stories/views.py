from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from django.utils import timezone
from datetime import timedelta

from .models import Story
from .serializers import StorySerializer
from follows.models import Follow
from django.contrib.auth import get_user_model

User = get_user_model()

class StoryViewSet(ModelViewSet):

    serializer_class = StorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        following_ids = Follow.objects.filter(
            follower=self.request.user
        ).values_list("following_id", flat=True)
    
        return Story.objects.filter(
            user_id__in=list(following_ids) + [self.request.user.id],
            expire_time__gt=timezone.now()
        ).select_related("user")

    

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    http_method_names = ['get', 'post', 'delete']

    @action(detail= False, methods= ['get'])
    def archive(self, request):    
        stories = Story.objects.filter(
            user=request.user,
            expire_time__lte=timezone.now()
        ).select_related("user")
        
        serializer = self.get_serializer(stories, many=True)
        return Response(serializer.data)