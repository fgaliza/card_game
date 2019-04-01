from django.conf import settings
from rest_framework import serializers

from .models import Battle, BattleRound, RoundResult


class RoundResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoundResult
        fields = (
            'player',
            'card',
            'score',
        )


class BattleRoundSerializer(serializers.ModelSerializer):
    results = RoundResultSerializer(many=True, read_only=True)

    class Meta:
        model = BattleRound
        fields = ('results', 'round_number')


class BattleSerializer(serializers.ModelSerializer):
    battle_rounds = BattleRoundSerializer(many=True, read_only=True)

    class Meta:
        model = Battle
        fields = ('players', 'battle_rounds',)

    def validate_players(self, value):
        if len(value) < 2:
            raise serializers.ValidationError(
                'At least two players required to play the game'
            )
        if len(value) > settings.MAX_NUMBER_OF_PLAYERS:
            raise serializers.ValidationError(
                'Maximum number of players exceeded'
            )
        return value
