from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):

    class Meta():
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    MOBILE = 'mobile'
    NOTEBOOK = 'notebook'
    PC = 'pc'
    ACC = 'accessories'
    CHOICE_GROUP = {
        (MOBILE, 'mobile'),
        (NOTEBOOK, 'notebook'),
        (PC, 'pc'),
        (ACC, 'accessories'),
    }
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    count = models.IntegerField()
    availability = models.BooleanField(default=True)
    group = models.CharField(max_length=20, choices=CHOICE_GROUP, default=MOBILE)
    img = models.ImageField(default='no_image.jpg', upload_to='product_image')
    basket = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return f'{self.name}'


class Customer(models.Model):
    name = models.CharField(max_length=64)
    nickname = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'


class Reviews(models.Model):
    text = models.TextField(max_length=2000)
    product_review = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE,
                                       related_name='comments_products', blank=True, null=True)

    def __str__(self):
        return f'{self.product_review}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
