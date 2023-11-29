from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from . import consumers


websocket_urlpatterns = [
    path('ws/chat/<int:chat_id>/', consumers.ChatConsumer.as_asgi()),
]

urlpatterns = [
    path('group-chats/', GroupChatListCreateView.as_view(), name='group-chat-list-create'),
    path('messages/', MessageListCreateView.as_view(), name='message-list-create'),
    path('user-profile/<int:pk>/', UserProfileDetailView.as_view(), name='user-profile-detail'),
    path('chat-list/', chat_list, name='chat_list'),
    path('create-chat/', create_chat, name='create_chat'),
    path('', index, name='index'),
    path('chat/<int:chat_id>/', chat_detail, name='chat_detail'),
    path('exit-chat/<int:chat_id>/', exit_chat, name='exit_chat'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('user-detail/<int:user_id>/', user_detail, name='user_detail'),
    path('send-private-message/<int:user_id>/', login_required(send_private_message), name='send_private_message'),
    path('private-messages/', login_required(view_private_messages), name='view_private_messages'),
]