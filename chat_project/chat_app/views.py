# chat_app/views.py
from rest_framework import generics
from .models import GroupChat, Message, UserProfile
from .serializers import GroupChatSerializer, MessageSerializer, UserProfileSerializer
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserProfileForm
from django.contrib.auth import login


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
def chat_detail(request, chat_id):
    chat = get_object_or_404(GroupChat, pk=chat_id)
    messages = Message.objects.filter(group_chat=chat).order_by('timestamp')
    members = chat.members.all()
    return render(request, 'chat_detail.html', {'chat': chat, 'messages': messages, 'members': members})



@login_required
def exit_chat(request, chat_id):
    chat = get_object_or_404(GroupChat, pk=chat_id)
    chat.members.remove(request.user)
    return redirect('chat_list')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        avatar_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and avatar_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password1'])
            user.save()

            profile = UserProfile.objects.create(user=user, avatar=request.FILES.get('avatar'))
            profile.save()

            login(request, user)
            return redirect('chat_list')
    else:
        user_form = UserRegistrationForm()
        avatar_form = UserProfileForm()

    return render(request, 'registration/register.html', {'user_form': user_form, 'avatar_form': avatar_form})


@login_required
def edit_profile(request):
    # Проверяем наличие UserProfile у пользователя
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        # Если UserProfile не существует, создаем его
        profile = UserProfile(user=request.user)
        profile.save()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('chat_list')  # Перенаправление на страницу профиля после успешного редактирования
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})