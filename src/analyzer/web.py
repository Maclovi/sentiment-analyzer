from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from analyzer import __version__
from analyzer.bootstrap import setup_routes
from analyzer.di import setup_all_providers


@asynccontextmanager
async def lifespan(app: FastAPI, /) -> AsyncIterator[None]:  # pragma: no cover
    yield None
    await app.state.dishka_container.close()


def create_web() -> FastAPI:
    container = make_async_container(*setup_all_providers())
    app = FastAPI(
        version=__version__,
        lifespan=lifespan,
        default_response_class=ORJSONResponse,
        root_path="/api",
    )
    setup_routes(app)
    setup_dishka(container=container, app=app)
    return app
