import factory

from apps.game_options.models import GameOptions


class GameOptionsFactory(factory.DjangoModelFactory):
    class Meta:
        model = GameOptions

    max_rounds_per_battle = 3
    number_of_initial_cards = 10
    max_number_of_players = 4
    number_of_cards_per_deck = 5
