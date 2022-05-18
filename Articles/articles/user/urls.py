from django.urls import path
from . import views
from django.contrib.auth import views as authViews

app_name = 'user'
urlpatterns = [
    path('', views.profile, name='profile'),
    path('login/', authViews.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('registration/', views.registration, name='registration'),
    path('<int:user_id>/', views.update_profile, name='update_profile'),
]
