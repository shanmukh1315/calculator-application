# tests/test_extra.py
from calc.cli import run_repl
import calc.cli as cli
import main as app_main

def make_input_fn(inputs, prompts=None):
    it = iter(inputs)
    prompts_list = prompts if prompts is not None else []
    def _inner(prompt=""):
        prompts_list.append(prompt)
        return next(it)
    return _inner

def test_cli_invalid_second_number():
    """Covers: second number invalid -> continue loop."""
    outputs = []
    inp = make_input_fn(["add", "2", "oops", "exit"])
    run_repl(input_fn=inp, output_fn=lambda s: outputs.append(s))
    joined = "\n".join(outputs)
    assert "Invalid number" in joined
    assert "Result:" not in joined

def test_cli_invalid_first_then_valid_flow():
    """Covers: first number invalid -> continue -> then a valid run."""
    outputs = []
    # attempt 1: invalid first number; attempt 2: valid addition; then exit
    inp = make_input_fn(["add", "abc", "add", "2", "3", "exit"])
    run_repl(input_fn=inp, output_fn=lambda s: outputs.append(s))
    joined = "\n".join(outputs)
    assert "Invalid number" in joined
    assert "Result: 5.0" in joined

def test_cli_unexpected_exception_branch(monkeypatch):
    """Forces the generic 'except Exception' branch."""
    outputs = []
    def boom(a, b):
        raise RuntimeError("boom")
    monkeypatch.setitem(cli.OPS, "add", boom)  # patch OPS['add'] to raise
    inp = make_input_fn(["add", "1", "2", "exit"])
    run_repl(input_fn=inp, output_fn=lambda s: outputs.append(s))
    assert any("An unexpected error occurred: boom" in line for line in outputs)

def test_cli_quit_alias():
    """Covers the 'quit' alias (you already covered 'exit')."""
    outputs = []
    inp = make_input_fn(["quit"])
    run_repl(input_fn=inp, output_fn=lambda s: outputs.append(s))
    assert any("Goodbye!" in line for line in outputs)

def test_main_invokes_run_repl(monkeypatch):
    """Covers the call inside main.main()."""
    called = []
    monkeypatch.setattr(app_main, "run_repl", lambda: called.append(True))
    app_main.main()
    assert called == [True]
