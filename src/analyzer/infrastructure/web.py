from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from analyzer import __version__
from analyzer.bootstrap import setup_routes


def create_app() -> FastAPI:
    app = FastAPI(
        default_response_class=ORJSONResponse,
        version=__version__,
        root_path="/api",
    )
    setup_routes(app)
    return app
