from typing import final

from typing_extensions import override

from analyzer.usecases import interfaces
from .annotations import Pipeline


@final
class PipelineAdapter(interfaces.SentimentNeural):
    def __init__(self, pipe: Pipeline) -> None:
        self._pipe = pipe

    @override
    def analyze(self, text: str) -> interfaces.AnalyzeOutput:
        return self._pipe(text)[0]
