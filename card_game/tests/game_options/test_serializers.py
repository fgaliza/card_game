import pytest

from apps.game_options.serializers import GameOptionsSerializer

pytestmark = pytest.mark.django_db


def test_game_options_detail_serializer(game_options_payload):
    serializer = GameOptionsSerializer(data=game_options_payload)
    serializer.is_valid()
    assert serializer.is_valid() is True
    assert serializer.data['max_rounds_per_battle'] == game_options_payload['max_rounds_per_battle']


def test_game_options_serializer_without_required_fields(game_options_payload):
    del game_options_payload['max_rounds_per_battle']
    serializer = GameOptionsSerializer(data=game_options_payload)
    assert serializer.is_valid() is False
