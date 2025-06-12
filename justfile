[doc("All command information")]
[group("Common")]
[private]
default:
  @just --list --unsorted --list-heading $'commands…\n'


[doc("Prepare venv and repo for developing")]
[group("Common")]
@bootstrap:
    cp .env.dist .env
    uv pip install -e ".[dev]"
    pre-commit install


[doc("Sync latest versions of packages")]
[group("Common")]
@venv-sync deps="dev":
    uv pip install -e ".[{{ deps }}]"


[doc("Run server application")]
[group("Common")]
@serve:
    python -m analyzer "--serve"


[doc("Lint check")]
[group("Linter and Static")]
@lint:
    echo "Run ruff check..." && ruff check --exit-non-zero-on-fix
    echo "Run ruff format..." && ruff format
    echo "Run codespell..." && codespell


[doc("Static analysis")]
[group("Linter and Static")]
@static:
    echo "Run mypy.." && mypy --config-file pyproject.toml
    echo "Run bandit..." && bandit -c pyproject.toml -r src
    echo "Run semgrep..." && semgrep scan --config auto --error


[doc("Run pre-commit all files")]
[group("Linter and Static")]
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


DOCKER_COMPOSE_FILE := "docker-compose.yml"

[doc("Run all containers")]
[group("Docker")]
@up:
  docker compose -f {{ DOCKER_COMPOSE_FILE }} --profile analyzer up --build -d --wait


[doc("Down all containers")]
[group("Docker")]
@down:
  docker compose -f {{ DOCKER_COMPOSE_FILE }} --profile analyzer down
  docker image prune -f
