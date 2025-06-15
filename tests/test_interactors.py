from unittest.mock import MagicMock

from analyzer.infrastructure.neural.adapters import PipelineAdapter
from analyzer.usecases.interactors import (
    SentimentAnalyzerHandler,
    SentimentInput,
)


def test_sentiment_analyzer_handler_with_fake_neural() -> None:
    mock_pipe = MagicMock(return_value=[{"label": "POSITIVE", "score": 0.9}])
    adapter = PipelineAdapter(mock_pipe)
    interactor = SentimentAnalyzerHandler(adapter)
    output = interactor.handle(SentimentInput("positive text"))

    assert output.label == "POSITIVE"
    assert output.score == 0.9  # noqa: PLR2004
