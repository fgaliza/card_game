import pytest
from django.conf import settings
from apps.battles.utils import (
    calculate_score,
    deal_cards,
    get_game_cards,
    prepare_rounds,
    save_battle_results,
    validate_player_cards,
)

from apps.cards.models import Card
from apps.battles.models import Battle

pytestmark = pytest.mark.django_db


@pytest.mark.parametrize(
    'number_of_players',
    [
        (2),
        (3),
        (4),
    ]
)
def test_get_game_cards(number_of_players, create_cards):
    cards_per_deck = settings.NUMBER_OF_CARDS_PER_DECK
    number_of_initial_cards = settings.NUMBER_OF_INITIAL_CARDS
    player_cards = cards_per_deck + number_of_initial_cards
    total_cards = number_of_players * player_cards
    game_cards = get_game_cards(number_of_players)
    assert len(game_cards) == total_cards
    assert len(game_cards) == len(set(game_cards))


@pytest.mark.parametrize(
    'number_of_players',
    [
        (2),
        (3),
        (4),
    ]
)
def test_deal_cards(number_of_players, create_cards):
    game_cards = get_game_cards(number_of_players)
    deck, hand = deal_cards(game_cards)
    assert len(deck) == settings.NUMBER_OF_CARDS_PER_DECK
    assert len(hand) == settings.NUMBER_OF_INITIAL_CARDS
    assert len(deck) == len(set(deck))
    assert len(hand) == len(set(hand))
    assert deck not in hand
    assert hand not in deck


def test_prepare_rounds():
    rounds = prepare_rounds()
    assert len(rounds) == settings.MAX_ROUNDS_PER_BATTLE


def test_calculate_score(round_result_payload):
    response = calculate_score(round_result_payload['results'])
    sorted_response = sorted(response, key=lambda i: i['score'], reverse=True)
    cards_played = [Card.objects.get(id=play['card']) for play in sorted_response]
    assert cards_played[1] in cards_played[0].stronger_than
    assert cards_played[2] in cards_played[0].stronger_than
    assert cards_played[0] in cards_played[1].weaker_than
    assert cards_played[2] in cards_played[1].stronger_than
    assert cards_played[0] in cards_played[2].weaker_than
    assert cards_played[1] in cards_played[2].weaker_than


def test_validate_player_cards(round_result_validated_data):
    assert validate_player_cards(round_result_validated_data['results'])


def test_validate_player_cards_invalid_card(round_result_validated_data):
    player = round_result_validated_data['results'][0]['player']
    card = round_result_validated_data['results'][0]['card']
    player.hand.remove(card)
    assert validate_player_cards(round_result_validated_data['results']) is False


@pytest.mark.parametrize(
    'result_index',
    [
        (0),
        (1),
        (2),
    ]
)
def test_save_battle_results(
    result_index,
    create_battle,
    round_result_validated_data,
):
    battle = Battle.objects.get(id=1)
    round_result_validated_data['results'][0]['player'] = battle.players.all()[0]
    round_result_validated_data['results'][1]['player'] = battle.players.all()[1]
    round_result_validated_data['results'][2]['player'] = battle.players.all()[2]
    current_round = battle.battle_rounds.first()
    save_battle_results(round_result_validated_data['results'], current_round)

    result = current_round.results.all()[result_index]
    expected_result = round_result_validated_data['results'][result_index]
    assert current_round.results.count() == 3
    assert result.player_id == expected_result['player'].id
    assert result.card_id == expected_result['card'].id
    assert result.score == expected_result['score']
