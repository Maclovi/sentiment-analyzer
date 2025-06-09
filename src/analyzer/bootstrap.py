from fastapi import APIRouter, FastAPI

from analyzer.presentation.v1.routes import healthcheck


def setup_routes(app: FastAPI, /) -> None:
    router_v1 = APIRouter(prefix="/v1")
    router_v1.include_router(healthcheck.router)

    app.include_router(router_v1)
