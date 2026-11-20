# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A beginner-friendly GUI calculator app built with Python and tkinter, designed to demonstrate vibe coding with Claude Code. No external dependencies — only the Python standard library is used.

## Commands

**Run the app:**
```bash
python3 calculator.py
```

**Run all tests:**
```bash
python3 -m unittest test_calculator.py -v
```

**Run a single test:**
```bash
python3 -m unittest test_calculator.TestCalculate.test_addition -v
```

## Architecture

The logic is split into two layers:

- **`calculate(expression)`** (`calculator.py`) — pure function that evaluates an expression string using `eval` and returns a string result or `"Error"`. This is the only testable unit.
- **`Calculator` class** (`calculator.py`) — tkinter GUI that owns the display and button layout. `on_click` handles all button presses: it builds `self.expression` character by character, calls `calculate()` on `=`, and clears on `C`.
- **`test_calculator.py`** — unit tests for `calculate()` only; the GUI class is not tested.
- **`main.py`** — standalone hello world script, unrelated to the calculator.
