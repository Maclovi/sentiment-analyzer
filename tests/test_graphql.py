from httpx import AsyncClient
from starlette import status


async def test_query(client: AsyncClient) -> None:
    json = {"query": "{ healthcheck }"}
    result = await client.post("/v1/graphql", json=json)

    assert result.status_code == status.HTTP_200_OK
    assert result.json()["data"] == {"healthcheck": "OK"}


async def test_mutation(client: AsyncClient) -> None:
    mutation = """
        mutation TestMutation($text: String!) {
            sentimentText(data: {text: $text}) {
                label
                score
            }
        }
    """
    json = {"query": mutation, "variables": {"text": "Good work!"}}
    result = await client.post(url="/v1/graphql", json=json)

    assert result.status_code == status.HTTP_200_OK
    data = result.json()["data"]
    assert data["sentimentText"] == {"label": "POSITIVE", "score": 0.9}
