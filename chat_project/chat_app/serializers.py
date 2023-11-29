from rest_framework import serializers
from .models import GroupChat, Message, UserProfile, PrivateMessage

class GroupChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupChat
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class PrivateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateMessage
        fields = ['id', 'sender', 'recipient', 'content', 'timestamp', 'is_read']