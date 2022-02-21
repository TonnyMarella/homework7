from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as authViews

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('registration/', include('users.urls')),
    path('login/', authViews.LoginView.as_view(template_name='users/login.html'), name='user'),
    path('exit/', authViews.LogoutView.as_view(template_name='main/index.html'), name='exit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
