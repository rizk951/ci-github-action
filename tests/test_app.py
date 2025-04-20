from src.app import add_numbers, calculate_average
import pytest

def test_add_numbers():
    """Test the add_numbers function with various inputs."""
    assert add_numbers(1, 2) == 3
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    assert add_numbers(100, 200) == 300

def test_calculate_average():
    """Test the calculate_average function with various inputs."""
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0
    assert calculate_average([-1, 0, 1]) == 0.0
    assert calculate_average([10, 20, 30]) == 20.0

def test_calculate_average_empty_list():
    """Test that calculate_average raises ValueError for empty list."""
    with pytest.raises(ValueError):
        calculate_average([]) 