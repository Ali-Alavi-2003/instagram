from django.urls import path
from rest_framework.routers import DefaultRouter

from accounts.views.users import(
    SendOtpAPIView,
    VerifyOtpAPIView,
)
from accounts.views.profile import(
    ProfileViewSet,
    AllProfileViewSet,
)

router = DefaultRouter()
router.register(
    prefix= 'profile',
    viewset= ProfileViewSet,
    basename= 'profile'
)
router.register(
    prefix= 'all-profiles',
    viewset= AllProfileViewSet,
    basename= 'all-profiles',
)

urlpatterns = [
    path('send-otp/', SendOtpAPIView.as_view(), name= 'send-otp'),
    path('verify-otp/', VerifyOtpAPIView.as_view(), name= 'verify-otp')
]+ router.urls 


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)