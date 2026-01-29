---
name: python
description: Use when writing, editing, or reviewing Python code; enforces type hints and scalable design patterns.
---

# Python

## General

- For complex python projects, use OOP and Dependency Injection pattern.
- Use `uv run` to execute Python scripts.
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
