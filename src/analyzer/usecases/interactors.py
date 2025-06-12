from typing import NamedTuple

from analyzer.usecases.interfaces import SentimentNeural


class SentimentInput(NamedTuple):
    text: str


class SentimentOutput(NamedTuple):
    label: str
    score: float


class SentimentAnalyzerHandler(NamedTuple):
    neural: SentimentNeural

    def handle(self, data: SentimentInput) -> SentimentOutput:
        result = self.neural.analyze(data.text)
        return SentimentOutput(**result)
