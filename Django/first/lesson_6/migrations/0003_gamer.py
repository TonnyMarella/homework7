# Generated by Django 4.0.2 on 2022-02-06 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_6', '0002_remove_gamemodel_eu_sales_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gamer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('games', models.ManyToManyField(to='lesson_6.GameModel')),
            ],
        ),
    ]
