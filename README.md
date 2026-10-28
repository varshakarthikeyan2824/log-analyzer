# Log Analyser

## Overview
A Python package that analyses log files and generates a JSON summary containing log-level counts, the most frequent errors, the time range, and the number of malformed lines.

## Features
- Counts log entries by severity level.
- Identifies the top five most frequent errors.
- Determines the start and end timestamps.
- Counts and reports malformed lines without crashing.
- Uses type hints, dataclasses, custom exceptions, and logging.
- Includes automated tests using pytest.
- Uses Ruff for linting and formatting, and Mypy for type checking.
- Uses pre-commit hooks to run quality checks before commits.

## Project Structure
```text
log-analyser/
├── src/log_analyser/
│   ├── __init__.py
│   ├── analyser.py
│   ├── parser.py
│   ├── models.py
│   └── exceptions.py
├── tests/
├── data/
│   └── messy.log
├── output/
│   └── summary.json
├── app.py
├── generate_logs.py
├── check_analyser.py
├── pyproject.toml
└── README.md
```

## Requirements
- Python 3.12+
- uv
- Git

## Setup
```bash
uv sync --dev
```

## Generate Sample Logs
```bash
uv run python generate_logs.py
```

## Run the Analyser
```bash
uv run python check_analyser.py
```

The JSON summary is saved to `output/summary.json`.

## Run Tests
```bash
uv run pytest
```

## Code Quality Checks
```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy src
uv run pre-commit run --all-files
```

## Output
The JSON report contains:
- `counts_by_level`: number of entries per log level.
- `top_errors`: the five most frequent error messages.
- `time_range`: earliest and latest valid timestamps.
- `bad_lines`: number of malformed log lines.

## Technologies
Python, uv, pytest, Ruff, Mypy, Git, and pre-commit.
