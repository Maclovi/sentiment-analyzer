from analyzer.infrastructure.neural.adapters import PipelineAdapter
from analyzer.infrastructure.neural.annotations import Pipeline
from analyzer.usecases.interactors import (
    SentimentAnalyzerHandler,
    SentimentInput,
)


def test_sentiment_analyzer_with_fake_neural(mock_pipe: Pipeline) -> None:
    adapter = PipelineAdapter(mock_pipe)
    interactor = SentimentAnalyzerHandler(adapter)
    output = interactor.handle(SentimentInput("positive text"))

    assert output.label == "POSITIVE"
    assert output.score == 0.9  # noqa: PLR2004
