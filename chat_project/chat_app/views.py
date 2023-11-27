# chat_app/views.py
from rest_framework import generics
from .models import GroupChat, Message, UserProfile
from .serializers import GroupChatSerializer, MessageSerializer, UserProfileSerializer
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


class GroupChatListCreateView(generics.ListCreateAPIView):
    queryset = GroupChat.objects.all()
    serializer_class = GroupChatSerializer

class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class UserProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

def index(request):
    return render(request, 'index.html')

# @login_required
def chat_list(request):
    chats = GroupChat.objects.all()
    return render(request, 'chat_list.html', {'chats': chats})


@login_required
def create_chat(request):
    if request.method == 'POST':
        chat_name = request.POST.get('chat_name')
        new_chat = GroupChat.objects.create(name=chat_name)
        new_chat.members.add(request.user)
        return redirect('chat_list')

    if request.user.is_anonymous:
        return HttpResponseForbidden("Forbidden. Please log in.")

    return render(request, 'create_chat.html')


@login_required
@login_required
def chat_detail(request, chat_id):
    chat = get_object_or_404(GroupChat, pk=chat_id)
    messages = Message.objects.filter(group_chat=chat).order_by('timestamp')
    return render(request, 'chat_detail.html', {'chat': chat, 'messages': messages})
