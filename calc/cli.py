"""REPL (Read–Eval–Print Loop) for the calculator.

Designed for testability via dependency-injected input/output callables.
"""
from __future__ import annotations
from typing import Callable, Dict
from .operations import add, subtract, multiply, divide

InputFn = Callable[[str], str]
OutputFn = Callable[[str], None]

OPS: Dict[str, callable] = {
    "+": add, "add": add,
    "-": subtract, "sub": subtract,
    "*": multiply, "mul": multiply,
    "/": divide, "div": divide,
}

HELP_TEXT = (
    "\nCalculator REPL\n"
    "Type an operation and then two numbers when prompted.\n"
    "Supported operations: +, -, *, / (or add, sub, mul, div).\n"
    "Type 'help' to see this message again, or 'exit' to quit.\n"
    "Examples: add 2 3 (via prompts), -, /, etc.\n"
)


def _get_number(prompt: str, input_fn: InputFn, output_fn: OutputFn) -> float | None:
    raw = input_fn(prompt).strip()
    try:
        return float(raw)
    except Exception:
        output_fn("Invalid number. Please enter a valid numeric value.")
        return None


def run_repl(input_fn: InputFn = input, output_fn: OutputFn = print) -> None:
    output_fn("Welcome to the Python Calculator! Type 'help' for instructions.")
    while True:
        op = input_fn("Operation (+, -, *, / | add, sub, mul, div | help | exit): ").strip().lower()
        if op in {"exit", "quit"}:
            output_fn("Goodbye!")
            break
        if op in {"help", "?"}:
            output_fn(HELP_TEXT)
            continue
        fn = OPS.get(op)
        if fn is None:
            output_fn(f"Unknown operation: {op!r}. Type 'help' for options.")
            continue
        a = _get_number("Enter first number: ", input_fn, output_fn)
        if a is None:
            continue
        b = _get_number("Enter second number: ", input_fn, output_fn)
        if b is None:
            continue
        try:
            result = fn(a, b)
            output_fn(f"Result: {result}")
        except ValueError as e:
            output_fn(str(e))
        except Exception as e:  # safety net
            output_fn(f"An unexpected error occurred: {e}")
