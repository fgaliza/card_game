import pytest
from django.db import IntegrityError

from apps.cards.models import Card

pytestmark = pytest.mark.django_db


def test_card_without_required_fields():
    with pytest.raises(IntegrityError):
        Card.objects.create(name='King',)


def test_card_duplicate_name():
    with pytest.raises(IntegrityError):
        Card.objects.create(name='King',)
        Card.objects.create(name='King',)


@pytest.mark.parametrize(
    'card_name, count',
    [
        ('Joker', 0),
        ('Soldier', 1),
        ('Soldier2', 1),
        ('King', 3),
    ]
)
def test_stronger_than_property(card_name, count, batch_create_cards):
    card = batch_create_cards[card_name]
    assert card.stronger_than.count() == count
    assert all([card.power > enemy.power for enemy in card.stronger_than])


@pytest.mark.parametrize(
    'card_name, count',
    [
        ('Joker', 3),
        ('Soldier', 1),
        ('Soldier2', 1),
        ('King', 0),
    ]
)
def test_weaker_than_property(card_name, count, batch_create_cards):
    card = batch_create_cards[card_name]
    assert card.weaker_than.count() == count
    assert all([card.power < enemy.power for enemy in card.weaker_than])


@pytest.mark.parametrize(
    'card_name, count',
    [
        ('Joker', 0),
        ('Soldier', 1),
        ('Soldier2', 1),
        ('King', 0),
    ]
)
def test_as_strong_as_property(card_name, count, batch_create_cards):
    card = batch_create_cards[card_name]
    assert card.as_strong_as.count() == count
    assert all([card.power == enemy.power for enemy in card.as_strong_as])
