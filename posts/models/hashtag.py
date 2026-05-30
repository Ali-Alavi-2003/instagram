from django.db import models
from django.conf import settings

from core.models import BaseModel
from posts.models.posts import Post

class Hashtag(BaseModel):
    body = models.CharField(max_length= 50, unique= True, db_index= True)
    posts = models.ManyToManyField(
        Post,
        related_name= 'hashtags',
    )