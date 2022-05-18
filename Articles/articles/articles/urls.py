from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as authViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('article.urls'), name='article'),
    path('user/', include('user.urls'), name='user'),
    path('exit/', authViews.LogoutView.as_view(), name='exit'),
]