from django.db import models


class GameModel(models.Model):
    name = models.CharField(max_length=64)
    platform = models.CharField(max_length=64)
    year = models.DateField()
    genre = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.id}_{self.name}_{self.genre}'


class Gamer(models.Model):
    games = models.ManyToManyField(GameModel)
    name = models.CharField(max_length=64)
    nickname = models.CharField(max_length=64)

