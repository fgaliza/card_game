import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from .factories import GameOptionsFactory

pytestmark = pytest.mark.django_db


def test_get_game_options(client):
    game_options = GameOptionsFactory()
    url = reverse('game-options:game-options-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['max_rounds_per_battle'] == game_options.max_rounds_per_battle


def test_create_game_options(client, game_options_payload):
    url = reverse('game-options:game-options-list')
    response = client.post(url, game_options_payload)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['max_rounds_per_battle'] == game_options_payload['max_rounds_per_battle']


def test_create_without_required_fields(client, game_options_payload):
    del game_options_payload['max_rounds_per_battle']
    url = reverse('game-options:game-options-list')
    response = client.post(url, game_options_payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
