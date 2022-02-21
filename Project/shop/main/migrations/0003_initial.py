# Generated by Django 4.0.2 on 2022-02-21 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0002_delete_subscribes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('nickname', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('count', models.IntegerField()),
                ('availability', models.BooleanField(default=True)),
                ('group', models.CharField(choices=[('notebook', 'notebook'), ('mobile', 'mobile'), ('pc', 'pc'), ('accessories', 'accessories')], default='mobile', max_length=20)),
                ('img', models.ImageField(default='no_image.jpg', upload_to='product_image')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField(max_length=2000)),
                ('product_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
