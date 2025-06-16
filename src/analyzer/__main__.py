import uvicorn

from analyzer.bootstrap import setup_configs
from analyzer.infrastructure.web import create_app_production


def run_web() -> None:
    configs = setup_configs()
    app = create_app_production()
    (host, port) = (configs.asgi.host, configs.asgi.port)
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    run_web()
