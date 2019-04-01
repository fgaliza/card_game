import pytest
from django.db import IntegrityError

from apps.players.models import Player

pytestmark = pytest.mark.django_db


def test_player_without_required_fields():
    with pytest.raises(IntegrityError):
        Player.objects.create(name=None)


def test_player_duplicate_name():
    with pytest.raises(IntegrityError):
        Player.objects.create(name='Player 1',)
        Player.objects.create(name='Player 1',)
