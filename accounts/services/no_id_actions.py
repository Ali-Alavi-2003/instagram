from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet


class NoIdActions:
    @action(detail= False, methods=['put'], url_path='update')
    def update_me(self, request):
        return self.update(request)
    
    @action(detail= False, methods=['patch'], url_path='partial-update')
    def partial_update_me(self, request):
        return self.partial_update(request)
    
    @action(detail= False, methods=['delete'], url_path='delete')
    def delete_me(self, request):
        return self.destroy(request)