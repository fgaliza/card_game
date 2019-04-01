import pytest

from apps.cards.serializers import CardDetailSerializer

pytestmark = pytest.mark.django_db


@pytest.fixture
def card_serializer():
    return CardDetailSerializer()


def test_card_detail_serializer(card_payload):
    serializer = CardDetailSerializer(data=card_payload)
    serializer.is_valid()
    assert serializer.is_valid() is True
    assert serializer.data['name'] == card_payload['name']
    assert serializer.data['power'] == str(card_payload['power'])


def test_card_serializer_without_required_fields(card_payload):
    del card_payload['power']
    serializer = CardDetailSerializer(data=card_payload)
    assert serializer.is_valid() is False
