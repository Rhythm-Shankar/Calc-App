"""Simple calculator functions with basic validation."""

from typing import Union

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """Return a + b."""
    return a + b

def subtract(a: Number, b: Number) -> Number:
    """Return a - b."""
    return a - b

def multiply(a: Number, b: Number) -> Number:
    """Return a * b."""
    return a * b

def divide(a: float, b: float) -> float:
    """Return the quotient of a divided by b. Raises ValueError if b is 0."""
    if b == 0:
        raise ValueError("Cannot divide by zero") 
    return a / b

