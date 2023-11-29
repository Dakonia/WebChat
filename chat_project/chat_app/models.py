# chat_app/models.py
from django.db import models
from django.contrib.auth.models import User

class GroupChat(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='group_chats')


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    group_chat = models.ForeignKey(GroupChat, null=True, blank=True, on_delete=models.CASCADE)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)



class PrivateMessage(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)