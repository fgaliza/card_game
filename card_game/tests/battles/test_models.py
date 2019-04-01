import pytest
from django.db import IntegrityError

from apps.battles.models import BattleRound

pytestmark = pytest.mark.django_db


def test_battle_round_without_required_fields():
    with pytest.raises(IntegrityError):
        BattleRound.objects.create(round_number=None,)
