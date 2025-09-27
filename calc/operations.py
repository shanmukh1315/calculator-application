"""Core arithmetic operations for the calculator.

Each function accepts two numeric (int or float) inputs and returns a float.
"""
from __future__ import annotations
from typing import Union

Number = Union[int, float]


def _to_float(x: Number) -> float:
    try:
        return float(x)
    except Exception as e:
        raise ValueError(f"Invalid numeric value: {x!r}") from e


def add(a: Number, b: Number) -> float:
    """Return a + b as float."""
    return _to_float(a) + _to_float(b)


def subtract(a: Number, b: Number) -> float:
    """Return a - b as float."""
    return _to_float(a) - _to_float(b)


def multiply(a: Number, b: Number) -> float:
    """Return a * b as float."""
    return _to_float(a) * _to_float(b)


def divide(a: Number, b: Number) -> float:
    """Return a / b as float. Raises ValueError on division by zero."""
    denom = _to_float(b)
    if denom == 0.0:
        raise ValueError("Division by zero is not allowed.")
    return _to_float(a) / denom
