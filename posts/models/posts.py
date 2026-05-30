from django.db import models
from django.conf import settings

from core.models import BaseModel

class Post(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE,
        related_name='posts',
    )

    img = models.ImageField(upload_to= 'posts/', null= True, blank= True)
    caption = models.TextField(
        max_length= 500,
        null= True,
        blank= True,
    )
    
    @property
    def like_count(self):
        return self.likes.count()
