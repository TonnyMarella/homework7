from django.urls import path
from . import views

urlpatterns = [
    path('try-form/', views.my_form, name='my_form'),
    path('try-modelform/', views.my_modelform, name='modelform'),
    path('simple-form/', views.simple_form, name='simple_form'),
]