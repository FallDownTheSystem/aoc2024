# Advent of Code 2024

Solutions for Advent of Code 2024 in Python.

## Project Structure

```
.
├── day1.py, day2.py, ...  # Daily solutions
├── aoc_helper.py          # Helper functions for fetching inputs
├── day.py                 # Template for new solutions
└── inputs/                # Puzzle inputs (not committed)
```

## Setup

1. Create a virtual environment and install dependencies:
```bash
uv venv
.venv\Scripts\activate  # On Windows
```
2. Get a session cookie from the AoC website and save it to environment variable: `AOC_SESSION_COOKIE`.

## Usage

1. Copy `day.py` to create a new solution file (e.g., `day1.py`).
2. Run tests with pytest:
```bash
uv run pytest day1.py -v
```
3. Run solution:
```bash
uv run day1.py
```

The `aoc_helper.py` module will automatically fetch and cache your puzzle input when you run a solution for the first time.
