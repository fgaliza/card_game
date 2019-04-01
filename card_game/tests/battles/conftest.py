import pytest

from .factories import BattleFactory
from tests.cards.factories import CardFactory
from tests.players.factories import PlayerFactory


@pytest.fixture
def create_players():
    return [
        PlayerFactory(id=1, name='Player 1'),
        PlayerFactory(id=2, name='Player 2'),
        PlayerFactory(id=3, name='Player 3'),
        PlayerFactory(id=4, name='Player 4'),
    ]


@pytest.fixture
def create_cards():
    return [CardFactory(name='Card{}'.format(index), power=index) for index in range(100)]


@pytest.fixture
def create_battle(create_players, create_cards):
    player_id_list = [player.id for player in create_players]
    return BattleFactory(players=player_id_list)


@pytest.fixture
def battle_payload(create_players):
    player_id_list = [player.id for player in create_players]
    return {
        'players': player_id_list,
        'battle_rounds': [
            {
                'round_results': [],
            },
            {
                'round_results': [],
            },
            {
                'round_results': [],
            },
        ]
    }


@pytest.fixture
def create_battle_payload(create_players):
    player_id_list = [player.id for player in create_players]
    return {
        'players': player_id_list
    }


@pytest.fixture
def battle_round_payload():
    return {
        'round_number': 1,
        'results': [
            {
                'results': []
            },
            {
                'results': []
            },
            {
                'results': []
            }
        ]
    }


@pytest.fixture
def round_result_payload(create_battle):
    players = create_battle.players.all()
    return {
        'results': [
            {
                'player': players[0].id,
                'card': players[0].hand.first().id,
            },
            {
                'player': players[1].id,
                'card': players[1].hand.first().id,
            },
            {
                'player': players[2].id,
                'card': players[2].hand.first().id,
            }
        ]
    }


@pytest.fixture
def round_result_validated_data():
    player1 = PlayerFactory(name='Player11')
    card1 = CardFactory(id=1000, name='MyCard1', power=10)
    player1.hand.add(card1)

    player2 = PlayerFactory(name='Player12')
    card2 = CardFactory(id=1001, name='MyCard2', power=20)
    player2.hand.add(card2)

    player3 = PlayerFactory(name='Player13')
    card3 = CardFactory(id=1002, name='MyCard3', power=30)
    player3.hand.add(card3)
    return {
        'results': [
            {
                'player': player1,
                'card': card1,
                'score': 1,
            },
            {
                'player': player2,
                'card': card2,
                'score': 2,
            },
            {
                'player': player3,
                'card': card3,
                'score': 3,
            }
        ]
    }
