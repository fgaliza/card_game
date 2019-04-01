import pytest

from apps.battles.serializers import BattleRoundSerializer, BattleSerializer

pytestmark = pytest.mark.django_db

# Battle


def test_battle_serializer(battle_payload):
    serializer = BattleSerializer(data=battle_payload)
    serializer.is_valid()
    assert serializer.is_valid() is True
    assert serializer.data['players'] == battle_payload['players']


def test_battle_serializer_without_required_fields(battle_payload):
    del battle_payload['players']
    serializer = BattleSerializer(data=battle_payload)
    assert serializer.is_valid() is False


def test_battle_serializer_with_1_player(battle_payload):
    battle_payload['players'] = [1]
    serializer = BattleSerializer(data=battle_payload)
    assert serializer.is_valid() is False


def test_battle_serializer_with_over_4_players(battle_payload):
    battle_payload['players'] = [1, 2, 3, 4, 5]
    serializer = BattleSerializer(data=battle_payload)
    assert serializer.is_valid() is False


# BattleRound

def test_battle_round_serializer(battle_round_payload):
    serializer = BattleRoundSerializer(data=battle_round_payload)
    assert serializer.is_valid() is True


def test_battle_round_serializer_without_required_fields(battle_round_payload):
    del battle_round_payload['round_number']
    serializer = BattleRoundSerializer(data=battle_round_payload)
    assert serializer.is_valid() is False
