import pytest
from django.db import IntegrityError

from apps.game_options.models import GameOptions

pytestmark = pytest.mark.django_db


def test_game_options_without_required_fields():
    with pytest.raises(IntegrityError):
        GameOptions.objects.create(max_rounds_per_battle=None)
