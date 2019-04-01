import pytest

from apps.players.serializers import PlayerSerializer

pytestmark = pytest.mark.django_db


@pytest.fixture
def player_serializer():
    return PlayerSerializer()


def test_player_detail_serializer(player_payload):
    serializer = PlayerSerializer(data=player_payload)
    serializer.is_valid()
    assert serializer.is_valid() is True
    assert serializer.data['name'] == player_payload['name']


def test_player_serializer_without_required_fields(player_payload):
    del player_payload['name']
    serializer = PlayerSerializer(data=player_payload)
    assert serializer.is_valid() is False
