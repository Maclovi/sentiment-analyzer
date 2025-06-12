from typing import cast, final

from transformers.pipelines import pipeline
from typing_extensions import override

from analyzer.usecases import interfaces


@final
class PipelineAdapter(interfaces.SentimentNeural):
    def __init__(self) -> None:
        self._pipe = pipeline("text-classification")

    @override
    def analyze(self, text: str) -> interfaces.AnalyzeOutput:
        return self._analyze(text)

    def _analyze(self, text: str) -> interfaces.AnalyzeOutput:
        result = self._pipe(text)[0]  # pyright: ignore[reportOptionalSubscript,reportIndexIssue]
        return cast("interfaces.AnalyzeOutput", result)
