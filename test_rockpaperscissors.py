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

