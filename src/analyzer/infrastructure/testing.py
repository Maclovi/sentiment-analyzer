import secrets
from typing import final
from unittest.mock import MagicMock

from typing_extensions import override

from analyzer.usecases import interfaces


@final
class PipelineAdapterTesting(interfaces.SentimentNeural):
    def __init__(self) -> None:
        binary = secrets.choice(["POSITIVE", "NEGATIVE"])
        score = secrets.randbelow(100) / 100
        self._pipe = MagicMock(
            return_value=[{"label": binary, "score": score}],
        )

    @override
    def analyze(self, text: str) -> interfaces.AnalyzeOutput:
        return self._analyze(text)

    def _analyze(self, text: str) -> interfaces.AnalyzeOutput:
        result = self._pipe(text)[0]
        return interfaces.AnalyzeOutput(
            label=result["label"],
            score=result["score"],
        )
