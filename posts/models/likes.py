from django.db import models
from django.conf import settings

from core.models import BaseModel
from posts.models.posts import Post


class Like(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE,
        related_name= 'likes',
    )
    post = models.ForeignKey(
        Post,
        on_delete= models.CASCADE,
        related_name= 'likes',
    )

    class Meta:
        unique_together = ('user', 'post')
        indexes = [
            models.Index(fields=['post', 'user']),
        ]