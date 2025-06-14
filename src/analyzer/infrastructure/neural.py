import logging
from collections.abc import Callable
from typing import TypeAlias, cast, final

from typing_extensions import override

from analyzer.usecases import interfaces

logger = logging.getLogger(__name__)
Pipe: TypeAlias = Callable[[str], list[interfaces.AnalyzeOutput]]


@final
class PipelineAdapter(interfaces.SentimentNeural):
    def __init__(self, *, pipe: Pipe | None = None) -> None:
        if pipe is None:
            try:
                from transformers.pipelines import pipeline
            except ImportError:
                logger.exception(
                    "Please, install transformers[torch]",
                )
                raise

            self._pipe = cast(
                "Pipe",
                pipeline(
                    "text-classification",
                    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
                ),
            )
        else:
            self._pipe = pipe

    @override
    def analyze(self, text: str) -> interfaces.AnalyzeOutput:
        return self._pipe(text)[0]
