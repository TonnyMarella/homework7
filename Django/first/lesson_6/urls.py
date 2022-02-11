from django.urls import path
from . import views

urlpatterns = [
    path('filter/', views.FilterView.as_view(), name='filter'),
    path('exclude/', views.ExcludeView.as_view(), name='exclude'),
    path('order_by/', views.OrderBy.as_view(), name='order_by'),
    path('union/', views.Union.as_view(), name='union'),
    path('values/', views.Values.as_view(), name='values'),
    path('filternum/', views.FilerNumView.as_view(), name='filternum'),
    path('all/', views.AllView.as_view(), name='all'),
    path('get/', views.get_view, name='get'),
]