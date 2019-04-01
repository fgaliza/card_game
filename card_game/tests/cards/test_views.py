from decimal import Decimal

import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from .factories import CardFactory

pytestmark = pytest.mark.django_db


def test_get_cards_return_none(client):
    url = reverse('cards:cards-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['results'] == []
    assert response.data['count'] == 0


def test_get_all_cards(client):
    card = CardFactory()
    url = reverse('cards:cards-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['results'][0]['name'] == card.name
    assert response.data['results'][0]['power'] == str(card.power)


def test_get_card_detail_by_id(client):
    card = CardFactory()
    url = reverse('cards:cards-detail', [card.id])
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == card.name
    assert response.data['power'] == str(card.power)


def test_get_card_detail_by_name(client):
    card = CardFactory()
    url = reverse('cards:cards-detail', [card.name])
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == card.name
    assert response.data['power'] == str(card.power)


def test_create_card(client, card_payload):
    url = reverse('cards:cards-list')
    response = client.post(url, card_payload)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['name'] == card_payload['name']
    assert response.data['power'] == str(card_payload['power'])


def test_create_without_required_fields(client, card_payload):
    del card_payload['name']
    url = reverse('cards:cards-list')
    response = client.post(url, card_payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_patch_card(client, card_payload):
    card = CardFactory()
    card_payload['power'] = Decimal('500.00')
    url = reverse('cards:cards-detail', [card.id])
    response = client.patch(url, card_payload)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['power'] == str(card_payload['power'])


def test_delete_card(client):
    card = CardFactory()
    url = reverse('cards:cards-detail', [card.id])
    response = client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
