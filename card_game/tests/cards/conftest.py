from decimal import Decimal

import pytest

from .factories import CardFactory


@pytest.fixture
def card_payload():
    return {
        'name': 'Joker',
        'power': Decimal('20.00'),
    }


@pytest.fixture
def batch_create_cards():
    cards_to_be_created = [
        {'name': 'Joker', 'power': Decimal('10.00'), },
        {'name': 'Soldier', 'power': Decimal('50.00'), },
        {'name': 'Soldier2', 'power': Decimal('50.00'), },
        {'name': 'King', 'power': Decimal('100.00'), },
    ]
    return {payload['name']: CardFactory(name=payload['name'], power=payload['power']) for payload in cards_to_be_created}
