---
name: python
description: Use when writing, editing, or reviewing Python code; enforces type hints and scalable design patterns.
---

## Python

- Use type hints for parameters, return types, and non-intuitive variables.
- For complex python projects, use OOP and Dependency Injection pattern.
- Use logging formats that include relative file path and line number so logs are clickable in VS Code (e.g. `%(filename)s:%(lineno)d`).
- Use `uv run` to execute Python scripts.
- Prefer `black` + `ruff` defaults unless the project specifies otherwise.
- Use absolute imports; avoid wildcard imports.
- Raise specific exceptions; avoid bare `except`.
- Prefer modern `typing`/`collections.abc` types; avoid `Any` unless justified.
- Document public functions and classes with docstrings.
