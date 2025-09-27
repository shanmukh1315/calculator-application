import pytest
from calc import add, subtract, multiply, divide

@pytest.mark.parametrize(
    "fn,a,b,expected",
    [
        (add, 2, 3, 5.0),
        (add, -1, 1.5, 0.5),
        (subtract, 10, 4, 6.0),
        (subtract, 3.5, 7, -3.5),
        (multiply, 6, 7, 42.0),
        (multiply, -2, 2.5, -5.0),
        (divide, 8, 2, 4.0),
        (divide, 7.5, 2.5, 3.0),
    ],
)
def test_operations_happy_path(fn, a, b, expected):
    assert fn(a, b) == pytest.approx(expected)

def test_divide_by_zero_raises():
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        divide(1, 0)

def test_invalid_numeric_raises():
    with pytest.raises(ValueError, match="Invalid numeric value"):
        add("abc", 1)  # exercises _to_float error branch for 100% coverage
