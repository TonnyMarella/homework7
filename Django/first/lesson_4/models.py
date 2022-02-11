# Вместо интернет магазина создал машины, автопарк и клиент, думаю это не существенно важная часть,
# но в случае чего могу переделать
from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    auto_description = models.TextField(null=True)
    year_of_manufacture = models.DateTimeField(auto_now_add=True, blank=True)
    ready_for_use = models.BooleanField(default=True)
    wiki_page = models.URLField(default="https://ru.wikipedia.org/", name='wikipedia')
    name = models.CharField(max_length=64, unique=True)
    photo_auto = models.ImageField(blank=True, null=True)
    price = models.FloatField(default=1.0)


class AutoPark(models.Model):
    count = models.IntegerField(default=0, blank=True)
    Year_of_opened = models.DateTimeField(auto_now_add=True, blank=True)
    photo_park = models.ImageField(blank=True, null=True)
    park_description = models.TextField(null=True)
    cars = models.ManyToManyField(Car, verbose_name='Auto-park')


class Clients(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    name = models.CharField(max_length=64)
    invoice = models.FileField()
    user_uuid = models.UUIDField(editable=False)
    discount_size = models.DecimalField(max_digits=10, decimal_places=10)
    client_ip = models.GenericIPAddressField(blank=True, null=True, protocol='IPv4')
