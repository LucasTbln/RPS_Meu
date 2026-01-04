import pytest
from src.RPSLS_Meu import GameAction, GameResult, assess_game


# Tests empate

@pytest.mark.parametrize("action", [
    GameAction.Rock,
    GameAction.Paper,
    GameAction.Scissors,
    GameAction.Lizard,
    GameAction.Spock
])
def test_draw(action):
    assert assess_game(action, action) == GameResult.Tie


# Tests pedra

def test_rock_beats_scissors():
    assert assess_game(GameAction.Rock, GameAction.Scissors) == GameResult.Defeat

def test_rock_beats_lizard():
    assert assess_game(GameAction.Rock, GameAction.Lizard) == GameResult.Defeat

def test_rock_loses_to_paper():
    assert assess_game(GameAction.Rock, GameAction.Paper) == GameResult.Victory

def test_rock_loses_to_spock():
    assert assess_game(GameAction.Rock, GameAction.Spock) == GameResult.Victory


# Tests papel

def test_paper_beats_rock():
    assert assess_game(GameAction.Paper, GameAction.Rock) == GameResult.Defeat

def test_paper_beats_spock():
    assert assess_game(GameAction.Paper, GameAction.Spock) == GameResult.Defeat

def test_paper_loses_to_scissors():
    assert assess_game(GameAction.Paper, GameAction.Scissors) == GameResult.Victory

def test_paper_loses_to_lizard():
    assert assess_game(GameAction.Paper, GameAction.Lizard) == GameResult.Victory


# Tests tesoiras

def test_scissors_beats_paper():
    assert assess_game(GameAction.Scissors, GameAction.Paper) == GameResult.Defeat

def test_scissors_beats_lizard():
    assert assess_game(GameAction.Scissors, GameAction.Lizard) == GameResult.Defeat

def test_scissors_loses_to_rock():
    assert assess_game(GameAction.Scissors, GameAction.Rock) == GameResult.Victory

def test_scissors_loses_to_spock():
    assert assess_game(GameAction.Scissors, GameAction.Spock) == GameResult.Victory


# Test lagarto

def test_lizard_beats_spock():
    assert assess_game(GameAction.Lizard, GameAction.Spock) == GameResult.Defeat

def test_lizard_beats_paper():
    assert assess_game(GameAction.Lizard, GameAction.Paper) == GameResult.Defeat

def test_lizard_loses_to_rock():
    assert assess_game(GameAction.Lizard, GameAction.Rock) == GameResult.Victory

def test_lizard_loses_to_scissors():
    assert assess_game(GameAction.Lizard, GameAction.Scissors) == GameResult.Victory


# Tests SPock

def test_spock_beats_scissors():
    assert assess_game(GameAction.Spock, GameAction.Scissors) == GameResult.Defeat

def test_spock_beats_rock():
    assert assess_game(GameAction.Spock, GameAction.Rock) == GameResult.Defeat

def test_spock_loses_to_paper():
    assert assess_game(GameAction.Spock, GameAction.Paper) == GameResult.Victory

def test_spock_loses_to_lizard():
    assert assess_game(GameAction.Spock, GameAction.Lizard) == GameResult.Victory
