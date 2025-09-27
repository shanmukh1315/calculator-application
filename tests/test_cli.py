from calc.cli import run_repl
import main as app_main  # to cover the main module

def make_input_fn(inputs, prompts=None):
    it = iter(inputs)
    prompts_list = prompts if prompts is not None else []
    def _inner(prompt=""):
        prompts_list.append(prompt)
        return next(it)
    return _inner

def test_cli_add_flow():
    outputs = []
    inp = make_input_fn(["add", "2", "3", "exit"])
    run_repl(input_fn=inp, output_fn=lambda s: outputs.append(s))
    joined = "\n".join(outputs)
    assert "Welcome to the Python Calculator" in joined
    assert "Result: 5.0" in joined
    assert "Goodbye!" in joined

def test_cli_unknown_operation():
    outputs = []
    inp = make_input_fn(["foo", "exit"])
    run_repl(input_fn=inp, output_fn=lambda s: outputs.append(s))
    assert any("Unknown operation" in line for line in outputs)

def test_cli_invalid_number_first_operand():
    outputs = []
    inp = make_input_fn(["add", "abc", "exit"])  # invalid first number, then exit
    run_repl(input_fn=inp, output_fn=lambda s: outputs.append(s))
    joined = "\n".join(outputs)
    assert "Invalid number" in joined
    assert "Result:" not in joined  # no result printed

def test_cli_division_by_zero_message():
    outputs = []
    inp = make_input_fn(["/", "5", "0", "exit"])  # divide by zero path
    run_repl(input_fn=inp, output_fn=lambda s: outputs.append(s))
    assert any("Division by zero" in line for line in outputs)

def test_cli_help():
    outputs = []
    inp = make_input_fn(["help", "exit"])  # show help, then exit
    run_repl(input_fn=inp, output_fn=lambda s: outputs.append(s))
    assert any("Calculator REPL" in line for line in outputs)

def test_main_io_covers_main_module():
    """Covers main.main_io so --cov=main reaches 100%."""
    outputs = []
    inp = make_input_fn(["exit"])
    app_main.main_io(input_fn=inp, output_fn=lambda s: outputs.append(s))
    assert any("Goodbye!" in line for line in outputs)
