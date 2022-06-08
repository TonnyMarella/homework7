from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as authViews
from rest_framework.routers import SimpleRouter
from django.conf import settings
from django.conf.urls.static import static
from article.views import ArticlesView


router = SimpleRouter()
router.register('api/articles', ArticlesView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('article.urls'), name='article'),
    path('user/', include('user.urls'), name='user'),
    path('exit/', authViews.LogoutView.as_view(), name='exit'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += router.urls
