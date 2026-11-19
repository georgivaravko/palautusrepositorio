# Repository Guidelines

## Scope

This guide applies only to `tdd-ostoskori/`, the shopping-cart TDD exercise.
Make changes within that directory and do not alter the other exercises in this
repository unless the task explicitly requires it.

## Project Structure & Module Organization

Source modules are in `tdd-ostoskori/src/`:

- `tuote.py` defines `Tuote`, a product with a name and price.
- `ostos.py` defines `Ostos`, an item and its quantity.
- `ostoskori.py` defines `Ostoskori`, the shopping-cart behavior.
- `index.py` is available for manual experimentation.

Tests live in `tdd-ostoskori/src/tests/`. Keep test modules there and name them
`*_test.py`, for example `ostoskori_test.py`. `pyproject.toml` and `uv.lock`
define the package environment and locked dependencies.

## Build, Test, and Development Commands

Use Python 3.14 or later. Run commands from `tdd-ostoskori/`:

```sh
cd tdd-ostoskori
uv sync          # install the locked development dependencies
uv run pytest    # run the full test suite
```

Run `uv run pytest` after each behavior change. Add a failing test first when
developing a new shopping-cart rule, then implement the smallest change that
makes it pass.

## Coding Style & Naming Conventions

Use four spaces for indentation. Follow the existing Finnish domain vocabulary:
classes use `PascalCase` (`Ostoskori`, `Tuote`) and modules, methods, and
variables use `snake_case` (`lisaa_tuote`, `tavaroita_korissa`). Keep public
method names consistent with the established API. Prefer small methods with one
clear responsibility. Add type annotations where they improve clarity, matching
the existing `Tuote` and `Ostos` constructor style. No formatter or linter is
configured; preserve the style of nearby code and avoid unrelated reformatting.

## Testing Guidelines

Tests use `pytest` to run `unittest.TestCase` classes. Name methods
`test_<expected_behavior>` and use `setUp` for shared fixtures. Test observable
cart behavior: item count, total price, adding and removing products, combining
identical products, and emptying the cart. Keep each test focused on one rule
and use clear product names and prices.

## Commit Guidelines

History uses short Finnish task-oriented messages, such as `viikko 1 tehtävä
15`. Use concise summaries that identify the exercise or behavior changed. Keep
each commit limited to this exercise and include the relevant tests with the
implementation.

## Users special requests:

Tests executed with uv run pytest
Code of ostos.py and tuote.py should not be changed
Tests should not be edited unless explicitly asked
Always implement absolutely minimal code that makes the tests pass