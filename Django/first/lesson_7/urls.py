from django.urls import include
from rest_framework import routers
from . import views
from django.urls import path


router = routers.SimpleRouter()
# Выводит все игры по году
router.register(r'game', views.GameViewSet)
# Выводит всех игроков
router.register(r'gamer', views.GamerViewSet)
# Выводит все игры, с возможностью удалять, обновлять, добавлять, искать по id и названию
router.register(r'all_actions_game', views.MyViewSets)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # выводит время
    path('time/', views.time, name='time'),
    path('time/kiev', views.time_kiev, name='time_kiev'),
    path('time/berlin', views.time_berlin, name='time_berlin'),
    # вытаскивает игры по id
    path('retrieve/<int:pk>', views.MyRetrieveAPIView.as_view(), name='retrieve'),
    path('ping/', views.PingAPI.as_view(), name='ping'),
    # регистрация
    path("register/", views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
]
