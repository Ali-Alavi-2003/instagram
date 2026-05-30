from django.db import models
from django.conf import settings

from core.models import BaseModel
from posts.models.posts import Post

class Profile(BaseModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE,
        related_name= 'profile',
    )
    avatar = models.ImageField(upload_to= 'profiles/', null= True, blank= True)
    bio = models.TextField(
        verbose_name= 'biography',
        max_length= 500,
        null= True,
        blank= True,
    )
    is_private = models.BooleanField(default= False)
    is_active = models.BooleanField(default= True)