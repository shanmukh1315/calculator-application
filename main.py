"""Entry points that launch the calculator REPL."""
from calc.cli import run_repl

def main_io(input_fn=input, output_fn=print) -> None:
    """Testable entry that allows injecting I/O (used by unit tests)."""
    run_repl(input_fn=input_fn, output_fn=output_fn)

def main() -> None:
    """Script entry when `python main.py` is executed."""
    run_repl()

if __name__ == "__main__":
    main()
