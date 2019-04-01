from rest_framework import serializers

from .models import GameOptions


class GameOptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = GameOptions
        fields = (
            'max_rounds_per_battle',
            'number_of_initial_cards',
            'max_number_of_players',
            'number_of_cards_per_deck',
            'created_at',
            'updated_at',
        )
