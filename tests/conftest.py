from collections.abc import AsyncIterator
from unittest.mock import MagicMock

import pytest
from dishka import Provider, Scope, make_async_container
from httpx import ASGITransport, AsyncClient

from analyzer.di import setup_all_providers
from analyzer.infrastructure.neural.annotations import Pipeline
from analyzer.web import create_web


def _fake_pipeline() -> Pipeline:
    return MagicMock(return_value=[{"label": "POSITIVE", "score": 0.9}])


@pytest.fixture(scope="session")
def mock_pipe() -> Pipeline:
    return _fake_pipeline()


@pytest.fixture(scope="session")
async def client() -> AsyncIterator[AsyncClient]:
    web = create_web()

    # override dependencies
    provider = Provider(scope=Scope.APP)
    provider.provide(_fake_pipeline, override=True)
    deps = (*setup_all_providers(), provider)
    web.state.dishka_container = make_async_container(*deps)

    t = ASGITransport(web)
    async with AsyncClient(transport=t, base_url="http://test") as ac:
        yield ac
