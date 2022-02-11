from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home-view'),
    path('book/', views.book, name='book'),
    path('book/<str:title>/', views.title, name='title'),
]