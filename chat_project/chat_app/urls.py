from django.urls import path
from .views import GroupChatListCreateView, MessageListCreateView, UserProfileDetailView, index, chat_list, create_chat, chat_detail
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
]