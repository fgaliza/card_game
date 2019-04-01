import random

import factory

from apps.cards.models import Card


class CardFactory(factory.DjangoModelFactory):
    class Meta:
        model = Card

    name = 'Joker'
    power = format(random.uniform(0, 100), '.2f')
