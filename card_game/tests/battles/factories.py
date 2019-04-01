import factory

from apps.battles.models import Battle, RoundResult


class BattleFactory(factory.DjangoModelFactory):
    class Meta:
        model = Battle

    players = [1, 2, 3, 4]

    @factory.post_generation
    def players(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for players in extracted:
                self.players.add(players)


class RoundResultFactory(factory.DjangoModelFactory):
    class Meta:
        model = RoundResult
