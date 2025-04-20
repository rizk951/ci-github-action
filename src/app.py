def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers together.
    
    Args:
        a (int): First number
        b (int): Second number
        
    Returns:
        int: Sum of the two numbers
    """
    return a + b

def calculate_average(numbers: list[float]) -> float:
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers (list[float]): List of numbers
        
    Returns:
        float: Average of the numbers
        
    Raises:
        ValueError: If the list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers) 