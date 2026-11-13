# Copilot instructions for viikko3/login

This file is specific to the `viikko3/login` Flask app. Keep all work scoped to this project unless a task explicitly requires another exercise in the repository.

## Local project setup

Run commands from this directory:

```bash
cd viikko3/login
uv sync
```

Start the app:

```bash
cd viikko3/login
uv run python src/index.py
```

The app listens on `http://localhost:5001`.

## Test and validation commands

This project uses Robot Framework browser tests rather than a Python unittest suite.

Run the full suite from the `viikko3/login` directory:

```bash
uv run robot src/test
```

Use this full-suite command for validation; do not narrow the run to an individual file or test case. The app must already be running before the tests execute; the suite accesses the app over HTTP on port `5001`.

## High-level architecture

The app is a small Flask application built in layers:

- `src/app.py`: route handlers and Flask app definition.
- `src/services/user_service.py`: business logic for login and registration validation.
- `src/repositories/user_repository.py`: in-memory repository for users.
- `src/entities/user.py`: the `User` data model.
- `src/templates/*.html`: Jinja templates for login, register, welcome, and main pages.
- `src/tests/*.robot`: end-to-end browser tests.
- `src/AppLibrary.py`: Robot helper that resets the app and creates users via HTTP requests.

The core pattern is: route -> service -> repository. The app stores state in memory only, and the `/tests/reset` endpoint is used to clear it between test runs.

## Project conventions

- This is an in-memory app. There is no database layer; state is kept in `UserRepository` while the server is running.
- Keep form field names, page titles, and button text aligned with the Robot tests. The tests rely on exact strings such as `id=username`, `id=password`, and `id=password_confirmation`.
- Validation rules are enforced in `UserService.validate()` and must stay consistent with the UI and tests:
  - username required
  - password required
  - minimum username length: 3
  - minimum password length: 8
  - password confirmation must match
  - username must be unique
- Browser tests are the primary validation mechanism. If you change the UI or routes, update or verify the matching Robot tests.
- Keep route-level behavior, service-level validation, repository logic, and template text in sync when making changes.

## Typical workflow

1. Start the app with `uv run python src/index.py`.
2. Run the full Robot suite with `uv run robot src/test`.
3. If the issue affects login or registration, check the route handler in `src/app.py` together with validation in `src/services/user_service.py`.
4. Verify the full Robot suite passes before considering the change complete.

This project is intentionally a small acceptance-test-driven Flask app; verify behavior through the browser tests rather than only by reading Python code in isolation.
