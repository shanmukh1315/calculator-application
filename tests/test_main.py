# tests/test_main.py
import main as app_main

def test_main_io_calls_run_repl(monkeypatch):
    # Simulate a single REPL cycle that immediately exits
    inputs = iter(["exit"])
    out = []
    def fake_input(prompt=""):
        return next(inputs)
    def fake_output(s: str):
        out.append(s)

    app_main.main_io(input_fn=fake_input, output_fn=fake_output)

    assert any("Welcome" in s for s in out)
    assert any("Goodbye!" in s for s in out)
