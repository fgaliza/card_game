import factory

from apps.players.models import Player


class PlayerFactory(factory.DjangoModelFactory):
    class Meta:
        model = Player

    name = 'Player 1'
