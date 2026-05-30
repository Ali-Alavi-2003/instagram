from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager

from core.models import BaseModel, CustomUserManager

class User(AbstractUser, BaseModel):
    username = None
    first_name = None
    last_name = None
    date_joined = None
    last_login = None
    
    phone_number = models.CharField(
        verbose_name= 'phone number',
        max_length= 11,
        unique= True,
    )

    objects = CustomUserManager()
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []