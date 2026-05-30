from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import timedelta

from core.models import BaseModel

# Create your models here.

class Story(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name= 'stories',
        on_delete= models.CASCADE,
    )
    img = models.ImageField(upload_to= 'stories/', null= True, blank= True)
    expire_time = models.DateTimeField(null= True, blank= True)
    
    def save(self, *args, **kwargs):
        if not self.expire_time:
            self.expire_time = (
                timezone.now() + timedelta(minutes= 10)
            )
        super().save(*args, **kwargs)
    
    @property
    def is_expired(self):
        return timezone.now() >= self.expire_time