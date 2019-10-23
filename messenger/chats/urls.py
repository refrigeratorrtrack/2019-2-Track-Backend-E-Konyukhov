from django.urls import path
from chats.views import index, chat_list, chat

urlpatterns = [
    path('index/', index, name='index'),
    path('', chat_list, name='chat_list'),
    path('chat/<int:chat_id>/', chat, name='chat'),
]
