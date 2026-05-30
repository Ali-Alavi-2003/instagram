from django.contrib import admin
from accounts.models.profile import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ...