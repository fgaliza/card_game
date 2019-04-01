import json

import pytest
from django.conf import settings
from rest_framework import status
from rest_framework.reverse import reverse

from .factories import RoundResultFactory

pytestmark = pytest.mark.django_db


def test_get_battles_return_none(client):
    url = reverse('battles:battles-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['results'] == []
    assert response.data['count'] == 0


def test_get_all_battles(client, create_players, create_cards, create_battle):
    battle_players = [player.id for player in create_battle.players.all()]
    url = reverse('battles:battles-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['results'][0]['players'] == battle_players


def test_get_battle_detail_by_id(client, create_players, create_cards, create_battle):
    battle_players = [player.id for player in create_battle.players.all()]
    url = reverse('battles:battles-detail', [create_battle.id])
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['players'] == battle_players


def test_create_battle(client, create_battle_payload, create_cards):
    url = reverse('battles:battles-list')
    response = client.post(url, create_battle_payload)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['players'] == create_battle_payload['players']


def test_create_battle_without_required_fields(client, create_battle_payload):
    del create_battle_payload['players']
    url = reverse('battles:battles-list')
    response = client.post(url, create_battle_payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_get_battle_results(client, create_battle):
    url = reverse('battles:battleround-list', kwargs={'nested_1_pk': create_battle.id})
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == settings.MAX_ROUNDS_PER_BATTLE
    assert [result['round_number'] for result in response.data] == [1, 2, 3]


@pytest.mark.parametrize(
    'round_id',
    [
        (1),
        (2),
        (3),
    ]
)
def test_get_battle_results_detail_by_id(round_id, client, create_battle):
    url = reverse(
        'battles:battleround-detail',
        [create_battle.id, round_id],
    )
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert 'results' in response.data


@pytest.mark.parametrize(
    'round_id',
    [
        (1),
        (2),
        (3),
    ]
)
def test_get_round_results_return_none(round_id, client, create_battle):
    url = reverse('battles:roundresult-list', [create_battle.id, round_id])
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == []


def test_get_round_results(client, create_battle):
    player = create_battle.players.first()
    card = player.hand.first()
    battle_round = create_battle.battle_rounds.first()
    round_result = RoundResultFactory(player=player, card=card)
    battle_round.results.add(round_result)
    url = reverse('battles:roundresult-list', [create_battle.id, 1])
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data[0]['player'] == player.id
    assert response.data[0]['card'] == card.id
    assert response.data[0]['score'] == 0


def test_create_round_result(client, round_result_payload):
    battle_id = 1
    round_number = 1
    url = reverse('battles:roundresult-list', [battle_id, round_number])
    response = client.post(url, json.dumps(round_result_payload), content_type='application/json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data[0]['player'] == round_result_payload['results'][0]['player']
    assert response.data[1]['player'] == round_result_payload['results'][1]['player']
    assert response.data[2]['player'] == round_result_payload['results'][2]['player']


def test_create_round_result_without_required_fields(client, round_result_payload):
    del round_result_payload['results'][0]['card']
    url = reverse('battles:battles-list')
    response = client.post(url, round_result_payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_get_players_hands(client, create_battle):
    url = reverse('battles:player-list', [1])
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['results'][0]['name'] == 'Player 1'
    assert response.data['results'][1]['name'] == 'Player 2'
    assert response.data['results'][2]['name'] == 'Player 3'
    assert response.data['results'][3]['name'] == 'Player 4'
    assert response.data['count'] == 4
