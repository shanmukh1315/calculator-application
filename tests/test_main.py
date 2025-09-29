# tests/test_main.py
import main as app_main

def test_main_io_calls_run_repl(monkeypatch):
    """Covers main_io() by injecting fake input/output."""
    inputs = iter(["exit"])
    out = []

    def fake_input(prompt=""):
        return next(inputs)

    def fake_output(s: str):
        out.append(s)

    app_main.main_io(input_fn=fake_input, output_fn=fake_output)

    assert any("Welcome" in s for s in out)
    assert any("Goodbye!" in s for s in out)

def test_main_invokes_run_repl(monkeypatch):
    """Covers the run_repl() call inside main()."""
    called = []
    # Patch the run_repl symbol imported in main.py
    monkeypatch.setattr(app_main, "run_repl", lambda: called.append(True))
    app_main.main()
    assert called == [True]
