from rockpaperscissors import get_winner

def test_player_wins():
    assert get_winner("rock", "scissors") == "player"
    assert get_winner("scissors", "paper") == "player"
    assert get_winner("paper", "rock") == "player"

def test_computer_wins():
    assert get_winner("rock", "paper") == "computer"
    assert get_winner("scissors", "rock") == "computer"
    assert get_winner("paper", "scissors") == "computer"

def test_draw():
    assert get_winner("rock", "rock") == "draw"
    assert get_winner("paper", "paper") == "draw"
    assert get_winner("scissors", "scissors") == "draw"

