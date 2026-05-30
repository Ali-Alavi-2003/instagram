from django.db import models
from django.conf import settings

from core.models import BaseModel


class DirectConversation(BaseModel):
    user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name= 'conversation',
    )

    class Meta:
        ordering = ["-created_at"]