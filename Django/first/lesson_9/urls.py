from django.urls import path
from . import views


urlpatterns = [
    path('security_test/', views.security_test, name='security_test'),
    path('ajax_url', views.ajax_check, name='ajax_url'),
]