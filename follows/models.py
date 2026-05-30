from django.db import models
from django.conf import settings

from core.models import BaseModel

# Create your models here.

class Follow(BaseModel):
    follower = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE,
        related_name= 'following',
    )
    following = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE,
        related_name= 'follower',
    )


    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['follower', 'following'],
                name='unique_follow_pair'
            )
        ]