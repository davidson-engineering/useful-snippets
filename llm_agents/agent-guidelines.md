# Agent Guidelines

## Logging
- Prefer logging calls as opposed to print statements, unless print statements are explicitly requested.
- Use appropriate logging levels (DEBUG, INFO, WARNING, ERROR, CRITICAL) based on the severity of the message.
- Log extra contextual information when available (e.g., user ID, request ID) to aid in debugging.

## Package Management
- Use uv for managing Python packages. Avoid using pip directly unless absolutely necessary.
- Use uv run python to execute commands inside python environment.
- A pyproject.toml file is used to manage dependencies. Ensure to update this file when adding or removing packages.
