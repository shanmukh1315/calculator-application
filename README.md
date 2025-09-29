# Calculator (CLI) — Assignment

[![Assignment CI – Calculator (Tests & Coverage)](https://github.com/shanmukh1315/calculator-application/actions/workflows/tests.yml/badge.svg)](https://github.com/shanmukh1315/calculator-application/actions/workflows/tests.yml)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

A robust command-line **calculator** with a REPL interface, full input validation & error handling, and **100% test coverage** enforced by GitHub Actions.

## Features

* **REPL** loop with prompts, `help`, and `exit`/`quit`
* **Operations:** add, subtract, multiply, divide (division-by-zero handled)
* **Input validation** and friendly error messages
* **Separation of concerns:** pure operations vs. CLI (DRY, testable)
* **CI:** tests run on every push; build fails if coverage < **100%**

## Project Structure

```
calculator-application/
├─ .github/workflows/tests.yml       # CI: pytest + coverage gate
├─ calc/
│  ├─ __init__.py
│  ├─ cli.py                         # REPL + prompts/validation
│  └─ operations.py                  # add/sub/mul/div
├─ tests/
│  ├─ conftest.py
│  ├─ test_cli.py
│  ├─ test_cli_more.py
│  ├─ test_extra.py
│  ├─ test_main.py
│  └─ test_operations.py             # parameterized tests
├─ main.py                           # entrypoints (main, main_io)
├─ pytest.ini                        # --cov-fail-under=100
├─ requirements.txt
└─ .gitignore
```

## Setup

Requires Python 3.9+.

```bash
python3 -m venv .venv
source .venv/bin/activate               # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

Example:

```
Welcome to the Python Calculator! Type 'help' for instructions.
Operation (+, -, *, / | add, sub, mul, div | help | exit): add
Enter first number: 2
Enter second number: 3
Result: 5.0
Operation (...): exit
Goodbye!
```

## Tests & Coverage (100%)

```bash
pytest
# or to see a detailed coverage table:
pytest -q --cov=calc --cov=main --cov-report=term-missing
```

## Continuous Integration

* Workflow: `.github/workflows/tests.yml`
* Triggers on **push** and **pull_request**
* Uses `pytest.ini` to **enforce 100% coverage** (build fails below 100%)

## Design Notes (Best Practices)

* **DRY & modular:** arithmetic in `operations.py`; user I/O in `cli.py`
* **Testability:** `main_io()` allows injecting input/output for REPL tests
* **Robust errors:** invalid numbers, unknown ops, divide-by-zero, and a generic exception path are handled and covered by tests
* **Parameterized tests** reduce duplication and increase coverage

