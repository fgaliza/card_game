from apps.utils.abstract_models import BaseModel, models


class GameOptions(BaseModel):
    max_rounds_per_battle = models.IntegerField()
    number_of_initial_cards = models.IntegerField()
    number_of_cards_per_deck = models.IntegerField()
    max_number_of_players = models.IntegerField()

    class Meta:
        verbose_name = 'Game Options'
        verbose_name_plural = 'Game Options'
