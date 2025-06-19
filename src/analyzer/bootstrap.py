import os

from fastapi import APIRouter, FastAPI

from analyzer.infrastructure.configs import ASGIConfig, Configs
from analyzer.presentation.v1.graphql import graphql
from analyzer.presentation.v1.routes import healthcheck, sentiment


def setup_configs() -> Configs:
    return Configs(
        asgi=ASGIConfig(
            host=os.getenv("ANALYZER_UVICORN_HOST", "localhost"),
            port=int(os.getenv("ANALYZER_UVICORN_PORT", "8008")),
        ),
    )


def setup_routes(app: FastAPI, /) -> None:
    router_v1 = APIRouter(prefix="/v1")
    router_v1.include_router(healthcheck.router)
    router_v1.include_router(sentiment.router)
    router_v1.include_router(graphql.router, prefix="/graphql")
    app.include_router(router_v1)
