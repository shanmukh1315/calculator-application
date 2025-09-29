from calc.cli import run_repl
import calc.cli as cli

def make_input_fn(inputs, prompts=None):
    it = iter(inputs)
    prompts_list = prompts if prompts is not None else []
    def _inner(prompt=""):
        prompts_list.append(prompt)
        return next(it)
    return _inner

def test_cli_invalid_second_number():
    outputs = []
    inp = make_input_fn(["add", "2", "oops", "exit"])
    run_repl(input_fn=inp, output_fn=lambda s: outputs.append(s))
    joined = "\n".join(outputs)
    assert "Invalid number" in joined
    assert "Result:" not in joined

def test_cli_unexpected_exception_branch(monkeypatch):
    outputs = []
    def boom(a, b):
        raise RuntimeError("boom")
    monkeypatch.setitem(cli.OPS, "add", boom)
    inp = make_input_fn(["add", "1", "2", "exit"])
    run_repl(input_fn=inp, output_fn=lambda s: outputs.append(s))
    assert any("An unexpected error occurred: boom" in line for line in outputs)
