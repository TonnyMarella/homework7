from django.urls import path
from . import views, post_view


urlpatterns = [
    path('main/', views.main, name='main'),
    path('main/luke/', views.luke, name='luke'),
    path('main/lea/', views.lea, name='lea'),
    path('main/xan/', views.xan, name='xan'),
    path('main/json/', views.json, name='json'),
    path('main/file/', views.file, name='file'),
    path('main/image/', views.image, name='image'),
    path('main/lets-do-it/', post_view.lets_do_it, name='lets_do_it'),
    path('main/heroes/', post_view.heroes, name='heroes'),
    path('main/heroes/<int:number>/', post_view.about, name='about'),
    path('main/rulers/', post_view.rulers, name='rulers'),

    path('class-view/', views.MyView.as_view(), name='class_view'),
]
