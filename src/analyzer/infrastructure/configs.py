from typing import NamedTuple


class ASGIConfig(NamedTuple):
    host: str
    port: int


class Configs(NamedTuple):
    asgi: ASGIConfig
