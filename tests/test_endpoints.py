from httpx import AsyncClient
from starlette import status


async def test_get_index(client: AsyncClient) -> None:
    response = await client.get("/v1/healthcheck")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "ok", "status": "success"}


async def test_sentiment_rest(client: AsyncClient) -> None:
    response = await client.post(
        "/v1/sentiment",
        json={"text": "Something good text"},
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"label": "POSITIVE", "score": 0.9}
