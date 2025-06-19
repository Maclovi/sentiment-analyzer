from typing import TYPE_CHECKING

import strawberry

from analyzer.usecases.interactors import (
    SentimentAnalyzerHandler,
    SentimentInput,
    SentimentOutput,
)

if TYPE_CHECKING:
    from dishka import AsyncContainer


@strawberry.input
class SentimentTextIn:
    text: str


@strawberry.type(name="SentimentOutput")
class SentimentTextProcessed:
    label: str
    score: float


@strawberry.type
class Mutation:
    @strawberry.mutation(graphql_type=SentimentTextProcessed)
    async def sentiment_text(
        self,
        data: SentimentTextIn,
        info: strawberry.Info,
    ) -> SentimentOutput:
        request = info.context["request"]
        container: AsyncContainer = request.state.dishka_container
        interactor = await container.get(SentimentAnalyzerHandler)
        return interactor.handle(SentimentInput(**data.__dict__))
