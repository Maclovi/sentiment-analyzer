from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from .annotations import Pipeline


def create_pipeline() -> "Pipeline":
    from transformers.pipelines import pipeline

    return cast(
        "Pipeline",
        pipeline(
            "text-classification",
            model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
        ),
    )
