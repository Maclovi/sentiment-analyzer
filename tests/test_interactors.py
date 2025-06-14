from unittest.mock import MagicMock

from analyzer.usecases.interactors import (
    SentimentAnalyzerHandler,
    SentimentInput,
)


def test_sentiment_analyzer_handler(pipeline_neural_fake: MagicMock) -> None:
    interactor = SentimentAnalyzerHandler(pipeline_neural_fake)
    output = interactor.handle(SentimentInput("positive text"))

    assert output.label in ("POSITIVE", "NEGATIVE")
    assert 0.0 <= output.score < 1.0
