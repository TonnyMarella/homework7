from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as authViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('article.urls'), name='article'),
    path('registration/', include('user.urls'), name='registration'),
    path('login/', authViews.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('exit/', authViews.LogoutView.as_view(), name='exit'),
]