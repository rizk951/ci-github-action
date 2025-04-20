from src.app import add_numbers

def test_add_numbers():
    """Test the add_numbers function with various inputs."""
    assert add_numbers(1, 2) == 3
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    assert add_numbers(100, 200) == 300 