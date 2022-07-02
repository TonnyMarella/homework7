from django.contrib import admin
from .models import Article, Comment, AuthorArticle

admin.site.register(Comment)
admin.site.register(AuthorArticle)


@admin.register(Article)
class ArcticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author_article')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    filter_horizontal = ['favorite']