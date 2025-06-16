from collections.abc import AsyncIterator

import pytest
from httpx import ASGITransport, AsyncClient

from analyzer.infrastructure.web import create_app


@pytest.fixture(scope="session")
async def client() -> AsyncIterator[AsyncClient]:
    t = ASGITransport(create_app())
    async with AsyncClient(transport=t, base_url="http://test") as ac:
        yield ac
