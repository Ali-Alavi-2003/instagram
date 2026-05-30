from django.urls import path, include
from rest_framework.routers import DefaultRouter

from posts.views.posts import PostViewset, AllPostViewset
from posts.views.saveposts import SavePostViewSet
from posts.views.hashtag import HashtagViewSet
from posts.views.comments import CommentModelViewset

router = DefaultRouter()
router.register(
    prefix= 'post',
    viewset= PostViewset,
    basename= 'post',
)

router.register(
    prefix= 'all-posts',
    viewset= AllPostViewset,
    basename= 'all-posts'
)

router.register(
    prefix='saved',
    viewset= SavePostViewSet,
    basename= 'saved',
)
router.register(
    prefix= 'tag',
    viewset= HashtagViewSet,
    basename= 'tag'
)
router.register(
    prefix= r'comments',
    viewset= CommentModelViewset,
    basename= 'comments'
)


urlpatterns = [
    path('', include(router.urls)),
]