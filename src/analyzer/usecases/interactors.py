from dataclasses import dataclass
from typing import final

from analyzer.usecases.interfaces import SentimentNeural


@dataclass(slots=True, frozen=True)
class SentimentInput:
    text: str


@dataclass(slots=True, frozen=True)
class SentimentOutput:
    label: str
    score: float


@final
class SentimentAnalyzerHandler:
    def __init__(self, neural: SentimentNeural) -> None:
        self._neural = neural

    def handle(self, data: SentimentInput) -> SentimentOutput:
        result = self._neural.analyze(data.text)
        return SentimentOutput(**result)
