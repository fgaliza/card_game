from django.db import models

from apps.cards.models import Card
from apps.players.models import Player


class RoundResult(models.Model):
    player = models.ForeignKey(
        Player,
        related_name='round_results',
        on_delete=models.CASCADE,
    )
    card = models.ForeignKey(
        Card,
        related_name='round_results',
        on_delete=models.CASCADE,
    )
    score = models.IntegerField(default=0)


class BattleRound(models.Model):
    results = models.ManyToManyField(
        RoundResult,
        related_name='battle_round',
    )
    round_number = models.IntegerField()


class Battle(models.Model):
    players = models.ManyToManyField(
        Player,
        related_name='battles',
    )
    battle_rounds = models.ManyToManyField(
        BattleRound,
        related_name='battles',
    )
