# chat_project/urls.py
from django.contrib import admin
from django.urls import path, include
from chat_app.views import chat_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('chat_app.urls')),
    path('', chat_list, name='home'),  # Добавляем новый URL-маршрут для главной страницы
]
