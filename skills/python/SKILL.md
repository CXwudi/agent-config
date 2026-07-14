---
name: python
description: Agent Skill for working with Python. Use when writing, editing, or reviewing Python code and scripts.
---

# Python

## General

- For complex python projects, use OOP and Dependency Injection pattern.
- Use `uv run` to execute Python scripts. Do not assume `python` or `python3` commands are available.
- For standalone or one-off python scripts, declare libraries within the script using PEP 723.
- Prefer `ty` + `ruff` defaults unless the project specifies otherwise.
- Use absolute imports; avoid wildcard imports.
- Raise specific exceptions; avoid bare `except`.
- Prefer `pytest` for tests.

## Logging

- Use the `logging` module with percent formatting (e.g. `logger.info("Processing %s items", count)`).
- Put a module-level logger at the top of each file (e.g. `logger = logging.getLogger(__name__)`).
- Use logging formats that include relative file path and line number so logs are clickable in VS Code (e.g. `%(filename)s:%(lineno)d`).

## Type Hints

- Use type hints for parameters, return types, and non-intuitive variables.
- Prefer modern `typing`/`collections.abc` types
- Try your best to avoid `Any` and `object` if possible; Call it out for scenarios that it is unavoidable
- If a variable is assigned from a library function call with no return type, such variable need a type hint
- Avoid `Protocol` for typing public facing APIs (specifically those that are mature) from third-party library.
- Avoid `typing.cast()` if possible
- Avoid `getattr()` if possible; prefer direct attribute/method access for known APIs.
