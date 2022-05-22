from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Reviews)


@admin.register(Product)
class Product(admin.ModelAdmin):
    filter_horizontal = ['basket']