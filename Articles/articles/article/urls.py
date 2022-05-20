from django.urls import path
from . import views

app_name = 'article'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/leave_comment/', views.leave_comment, name='leave_comment'),
    path('search/', views.search, name='search'),
    path('sort/', views.sort_by_alphabet, name='sort_by_alphabet'),
    path('favorite/', views.favorite, name='favorite')
]
