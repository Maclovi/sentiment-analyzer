from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter

from analyzer.usecases.interactors import (
    SentimentAnalyzerHandler,
    SentimentInput,
    SentimentOutput,
)

router = APIRouter(
    prefix="/sentiment",
    tags=["Sentiment"],
    route_class=DishkaRoute,
)


@router.post("", summary="Sentiment analyzer text")
async def sentiment_text(
    data: SentimentInput,
    interactor: FromDishka[SentimentAnalyzerHandler],
) -> SentimentOutput:
    return interactor.handle(data)
