from django.db import models
from django.conf import settings

from core.models import BaseModel
from posts.models.posts import Post


class SavePost(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE,
    )
    post= models.ForeignKey(
        Post,
        related_name= 'savepost',
        on_delete= models.CASCADE,
    )