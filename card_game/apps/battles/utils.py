from django.conf import settings
from django.db import transaction

from apps.battles.models import BattleRound, RoundResult
from apps.cards.models import Card


def get_game_cards(number_of_players):
    cards_per_deck = settings.NUMBER_OF_CARDS_PER_DECK
    number_of_initial_cards = settings.NUMBER_OF_INITIAL_CARDS
    player_cards = cards_per_deck + number_of_initial_cards
    total_cards = number_of_players * player_cards
    random_cards = Card.objects.all().order_by('?')
    card_ids = random_cards.values_list('id', flat=True)[:total_cards]
    return [card for card in card_ids]


def deal_cards(game_cards):
    deck = []
    hand = []
    for i in range(settings.NUMBER_OF_CARDS_PER_DECK):
        deck.append(game_cards.pop())
    for i in range(settings.NUMBER_OF_INITIAL_CARDS):
        hand.append(game_cards.pop())
    return deck, hand


def prepare_rounds():
    rounds = []
    for i in range(1, (settings.MAX_ROUNDS_PER_BATTLE + 1)):
        blank_round = BattleRound.objects.create(round_number=i)
        rounds.append(blank_round.id)
    return rounds


def calculate_score(players_actions):
    cards_played = Card.objects.filter(
        id__in=[action['card'] for action in players_actions],
    )
    response = []
    for player in players_actions:
        player_card = cards_played.get(id=player['card'])
        oponents = cards_played.exclude(id=player_card.id)
        player['score'] = 0
        for oponent in oponents:
            if player_card.power > oponent.power:
                player['score'] += 1
            elif player_card.power < oponent.power:
                player['score'] -= 1
        response.append(player)
    return response


def validate_player_cards(players_actions):
    return all([player['player'].hand.filter(id=player['card'].id).exists() for player in players_actions])


def save_battle_results(serializer_data, current_round):
    with transaction.atomic():
        result_list = [RoundResult.objects.create(**r) for r in serializer_data]
        current_round.results.set(result_list)
        current_round.save()
