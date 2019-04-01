from rest_framework import serializers

from .models import Player
from apps.cards.serializers import CardSimpleSerializer


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ('name',)


class PlayerHandSerializer(serializers.ModelSerializer):
    hand = CardSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = ('name', 'hand',)
