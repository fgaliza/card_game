from apps.cards.models import Card
from apps.utils.abstract_models import BaseModel, models


class Player(BaseModel):

    name = models.CharField(max_length=64, unique=True, blank=False)
    deck = models.ManyToManyField(Card, related_name='player_deck')
    hand = models.ManyToManyField(Card, related_name='player_hand')

    class Meta:
        ordering = ('name',)
