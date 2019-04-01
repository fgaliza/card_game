from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver

from .models import Battle
from .utils import deal_cards, get_game_cards, prepare_rounds
from apps.battles.models import RoundResult
from apps.players.models import Player


@receiver(m2m_changed, sender=Battle.players.through)
def battle_preparations(sender, instance, action, model, pk_set, **kwargs):
    if action == 'post_add':
        game_cards = get_game_cards(number_of_players=len(pk_set))

        for pk in pk_set:
            player = Player.objects.get(id=pk)
            deck, hand = deal_cards(game_cards)
            player.deck.set(deck)
            player.hand.set(hand)
            player.save()
        instance.battle_rounds.set(prepare_rounds())
        instance.save()


@receiver(post_save, sender=RoundResult)
def update_player_cards(sender, instance, **kwargs):
    new_card = instance.player.deck.first()
    instance.player.deck.remove(new_card)
    instance.player.hand.remove(instance.card)
    instance.player.hand.add(new_card)
    instance.player.save()
