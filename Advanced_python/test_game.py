import pytest
from game import Game

@pytest.fixture
def game_instance():
    """Fixture to create a new Game instance for each test."""
    return Game()

def test_initial_score(game_instance):
    """Test that the initial score is zero."""
    assert game_instance.score == 0

def test_game_over_initial_state(game_instance):
    """Test that the game is not over initially."""
    assert not game_instance.is_game_over()

def test_get_final_score_before_game_over(game_instance):
    """Test that calling get_final_score before the game is over raises an error."""
    with pytest.raises(ValueError, match="Game is not over yet."):
        game_instance.get_final_score()

def test_set_game_over_and_get_final_score(game_instance):
    """Test setting the game over state and retrieving the final score."""
    game_instance._game_over = True  # Simulate game over
    game_instance.score = 10  # Simulate a score
    assert game_instance.get_final_score() == 10
