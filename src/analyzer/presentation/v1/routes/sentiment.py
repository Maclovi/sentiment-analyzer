from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter

from analyzer.usecases.interactors import (
    SentimentAnalyzerHandler,
    SentimentInput,
    SentimentOutput,
)

route = APIRouter(
    prefix="/sentiment",
    tags=["Sentiment"],
    route_class=DishkaRoute,
)


@route.post("", summary="Sentiment analyzer text")
async def sentiment_text(
    text: str,
    interactor: FromDishka[SentimentAnalyzerHandler],
) -> SentimentOutput:
    return interactor.handle(SentimentInput(text))
