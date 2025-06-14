from collections.abc import AsyncIterator

import pytest
from httpx import ASGITransport, AsyncClient
from starlette import status

from analyzer.web import create_app_production


@pytest.fixture(scope="session")
async def client() -> AsyncIterator[AsyncClient]:
    t = ASGITransport(create_app_production())
    async with AsyncClient(transport=t, base_url="http://test") as ac:
        yield ac


async def test_get_index(client: AsyncClient) -> None:
    response = await client.get("/v1/healthcheck/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "ok", "status": "success"}
