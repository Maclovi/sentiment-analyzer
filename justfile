[doc("All command information")]
[private]
default:
  @just --list --unsorted --list-heading $'commands…\n'


[doc("Prepare venv and repo for developing")]
@bootstrap:
    uv pip install -e ".[dev]"
    pre-commit install


[doc("Sync latest versions of packages")]
@venv-sync:
    uv pip install -e ".[dev]"


[doc("Run server application")]
@serve:
    analyzer "--serve"


[doc("Lint check")]
@lint:
    echo "Run ruff check..." && ruff check --exit-non-zero-on-fix
    echo "Run ruff format..." && ruff format
    echo "Run codespell..." && codespell


[doc("Static analysis")]
@static:
    echo "Run mypy.." && mypy --config-file pyproject.toml
    echo "Run bandit..." && bandit -c pyproject.toml -r src
    echo "Run semgrep..." && semgrep scan --config auto --error


[doc("Run pre-commit all files")]
@pre-commit:
    pre-commit run --show-diff-on-failure --color=always --all-files


[doc("Run test")]
[group("Test")]
@test *args:
    coverage run -m pytest -x --ff {{ args }}
    just stop


[doc("Run test with coverage")]
[group("Test")]
@cov: test
    coverage combine
    coverage report --show-missing --skip-covered --sort=cover --precision=2
    rm .coverage*
