from django.db import models
from django.conf import settings

from core.models import BaseModel
from directs.models.directconversations import DirectConversation

class DirectMessage(BaseModel):
    conversation = models.ForeignKey(
        DirectConversation,
        on_delete= models.CASCADE,
        related_name= 'message',
    )
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE,
        related_name= 'message',
    )
    message = models.TextField(blank= True)
    file = models.FileField(upload_to= 'chats/', null= True, blank= True,)


    class Meta:
        ordering = ["created_at"]