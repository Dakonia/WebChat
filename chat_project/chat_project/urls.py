from django.contrib import admin
from django.urls import path, include
from chat_app.views import chat_list
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('chat_app.urls')),
    path('', chat_list, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)