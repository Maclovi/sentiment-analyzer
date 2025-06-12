from typing import Protocol, TypedDict


class AnalyzeOutput(TypedDict):
    label: str
    score: float


class SentimentNeural(Protocol):
    def analyze(self, text: str) -> AnalyzeOutput:
        raise NotImplementedError
