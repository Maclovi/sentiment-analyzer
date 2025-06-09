FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder
WORKDIR /app

COPY ./pyproject.toml ./justfile ./
COPY ./src ./src

RUN uv pip install --system --no-cache --target dependencies "."


FROM python:3.12-slim as production
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "/app/dependencies"

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    mkdir -p /usr/local/bin && \
    curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to /usr/local/bin && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY --from=builder /app/ ./
