import pytest


@pytest.fixture
def game_options_payload():
    return {
        'max_rounds_per_battle': 5,
        'number_of_initial_cards': 5,
        'max_number_of_players': 5,
        'number_of_cards_per_deck': 5,
    }
