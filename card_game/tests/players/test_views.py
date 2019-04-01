import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from .factories import PlayerFactory

pytestmark = pytest.mark.django_db


def test_get_player_return_none(client):
    url = reverse('players:players-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['results'] == []
    assert response.data['count'] == 0


def test_get_all_players(client):
    player = PlayerFactory()
    url = reverse('players:players-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['results'][0]['name'] == player.name


def test_get_player_detail_by_id(client):
    player = PlayerFactory()
    url = reverse('players:players-detail', [player.id])
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == player.name


def test_create_player(client, player_payload):
    url = reverse('players:players-list')
    response = client.post(url, player_payload)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['name'] == player_payload['name']


def test_create_without_required_fields(client, player_payload):
    del player_payload['name']
    url = reverse('players:players-list')
    response = client.post(url, player_payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_patch_player(client, player_payload):
    player = PlayerFactory()
    player_payload['name'] = 'Player10'
    url = reverse('players:players-detail', [player.id])
    response = client.patch(url, player_payload)
    assert response.status_code == status.HTTP_200_OK


def test_delete_player(client):
    player = PlayerFactory()
    url = reverse('players:players-detail', [player.id])
    response = client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
