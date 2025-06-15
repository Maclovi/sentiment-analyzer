from typing import TYPE_CHECKING, cast

from transformers.pipelines import pipeline

if TYPE_CHECKING:
    from .annotations import Pipeline


def create_pipeline() -> "Pipeline":
    return cast(
        "Pipeline",
        pipeline(
            "text-classification",
            model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
        ),
    )
