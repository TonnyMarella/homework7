from .models import GameModel, Gamer
from rest_framework import serializers


class GameModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameModel
        fields = '__all__'
        lookup_field = 'name'
        extra_kwargs = {
            'url': {'lookup_field': 'name'}
        }


class GamerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gamer
        fields = ['nickname', 'name']

