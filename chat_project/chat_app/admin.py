from django.contrib import admin
from .models import GroupChat, UserProfile, Message

admin.site.register(GroupChat)
admin.site.register(UserProfile)
admin.site.register(Message)
