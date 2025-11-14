from rockpaperscissors import get_winner

def test_player_wins():
    assert get_winner("rock", "scissors") == "player"
    assert get_winner("scissors", "paper") == "player"
    assert get_winner("paper", "rock") == "player"

