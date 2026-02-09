---
name: python
description: Agent Skill for working with Python. Use when writing, editing, or reviewing Python code and scripts.
---

# Python

## General

- For complex python projects, use OOP and Dependency Injection pattern.
- Use `uv run` to execute Python scripts. Do not assume `python` or `python3` commands are available.
- Prefer `black` + `ruff` defaults unless the project specifies otherwise.
- Use absolute imports; avoid wildcard imports.
- Raise specific exceptions; avoid bare `except`.
- Prefer `pytest` for tests.
- Document public functions and classes with docstrings.

## Logging

- Use the `logging` module with percent formatting (e.g. `logger.info("Processing %s items", count)`).
- Put a module-level logger at the top of each file (e.g. `logger = logging.getLogger(__name__)`).
- Use logging formats that include relative file path and line number so logs are clickable in VS Code (e.g. `%(filename)s:%(lineno)d`).

## Type Hints

- Use type hints for parameters, return types, and non-intuitive variables.
- Prefer modern `typing`/`collections.abc` types; avoid `Any` unless justified.
