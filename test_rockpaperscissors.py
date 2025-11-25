import pytest
from rockpaperscissors import get_winner, get_computer_option, options

def test_player_wins():
    assert get_winner("rock", "scissors") == "player"
    assert get_winner("paper", "rock") == "player"
    assert get_winner("scissors", "paper") == "player"

def test_computer_wins():
    assert get_winner("rock", "paper") == "The computer wins! You lose!"
    assert get_winner("paper", "scissors") == "The computer wins! You lose!"
    assert get_winner("scissors", "rock") == "The computer wins! You lose!"

def test_draw():
    assert get_winner("rock", "rock") == "It's a draw! Play again."
    assert get_winner("paper", "paper") == "It's a draw! Play again."
    assert get_winner("scissors", "scissors") == "It's a draw! Play again."

def test_invalid_inout():
    with pytest.raises(ValueError):
        get_winner("Blue", "rock")

#test if computer gives a correct input
def test_computer_input():
#making sure computer input is limited to 3 options: rock,paper,scissors
    for _ in range(50):
        assert get_computer_option() in options
