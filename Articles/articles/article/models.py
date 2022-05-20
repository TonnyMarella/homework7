from django.db import models
from django.contrib.auth.models import User


class AuthorArticle(models.Model):
    class Meta():
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'


class Article(models.Model):
    class Meta():
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['create']

    title = models.CharField('Название', max_length=50)
    text = models.TextField('Содержимое', )
    create = models.DateTimeField('Создано', auto_now_add=True)
    author_article = models.ForeignKey(AuthorArticle, on_delete=models.CASCADE, default=1)
    favorite = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    class Meta():
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('Имя автора', max_length=50)
    comment_text = models.CharField('Комментарий', max_length=200)

    def __str__(self):
        return f'{self.author_name}'
