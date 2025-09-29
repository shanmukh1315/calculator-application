# tests/test_cli_more.py
from calc.cli import run_repl

def make_input_fn(inputs, prompts=None):
    it = iter(inputs)
    prompts_list = prompts if prompts is not None else []
    def _inner(prompt=""):
        prompts_list.append(prompt)
        return next(it)
    return _inner

def test_cli_unknown_operation():
    outputs = []
    inp = make_input_fn(["foo", "exit"])
    run_repl(input_fn=inp, output_fn=lambda s: outputs.append(s))
    assert any("Unknown operation" in line for line in outputs)

def test_cli_help_branch():
    outputs = []
    inp = make_input_fn(["help", "exit"])
    run_repl(input_fn=inp, output_fn=lambda s: outputs.append(s))
    assert any("Calculator REPL" in line for line in outputs)

def test_cli_invalid_first_number():
    outputs = []
    inp = make_input_fn(["add", "abc", "exit"])
    run_repl(input_fn=inp, output_fn=lambda s: outputs.append(s))
    joined = "\n".join(outputs)
    assert "Invalid number" in joined
    assert "Result:" not in joined  # no result printed on invalid input

def test_cli_division_by_zero_message():
    outputs = []
    inp = make_input_fn(["/", "5", "0", "exit"])
    run_repl(input_fn=inp, output_fn=lambda s: outputs.append(s))
    assert any("Division by zero" in line for line in outputs)
