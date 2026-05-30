from django.db import models
from django.conf import settings

from core.models import BaseModel
from posts.models.posts import Post


class Comment(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE,
        related_name= 'comments',
    )
    post = models.ForeignKey(
        Post,
        on_delete= models.CASCADE,
        related_name= 'comments',
    )
    comment = models.ForeignKey(
        'self',
        on_delete= models.CASCADE,
        related_name= 'reply',
        blank= True,
        null= True,
    )
    text = models.TextField(max_length= 300,)