from django.contrib import admin
from .models import Article, Comment, AuthorArticle

admin.site.register(Comment)
admin.site.register(AuthorArticle)


@admin.register(Article)
class ArcticleAdmin(admin.ModelAdmin):
    filter_horizontal = ['favorite']