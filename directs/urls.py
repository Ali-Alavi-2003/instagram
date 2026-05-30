from django.urls import path, include
from rest_framework.routers import DefaultRouter

from directs.views.direct import (
    DirectConversationViewSet,
    DirectMessageViewSet,
)

router = DefaultRouter()
router.register(
    "conversations",
    DirectConversationViewSet,
    basename="conversations"
)

router.register(
    "messages",
    DirectMessageViewSet,
    basename="messages"
)

urlpatterns = [
    path('', include(router.urls))
]
