from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.response import Response

from accounts.models.profile import Profile
from accounts.serializer.profile import ProfileSerializer
from core.services.extend_actions import ExtendActions

class ProfileViewSet(ExtendActions, ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.select_related('user').filter(user=self.request.user)

    def get_object(self):
        return self.get_queryset().first()

    @action(detail=False, methods=['get', 'put', 'patch'], url_path='me')
    def me(self, request):
        
        instance = self.get_object()
        
        if request.method == 'GET':
            serializer = self.get_serializer(instance)
            return Response(serializer.data)

        partial = (request.method == 'PATCH')
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class AllProfileViewSet(ExtendActions, ModelViewSet):

    serializer_class = ProfileSerializer
    queryset = Profile.objects.all().select_related('user')
    filter_backends = [SearchFilter]
    search_fields = ['user__username']
