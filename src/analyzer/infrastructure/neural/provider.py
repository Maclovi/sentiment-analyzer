from typing import cast

from .annotations import Pipeline  # noqa: TC001


def create_pipeline() -> "Pipeline":
    from transformers.pipelines import pipeline

    return cast(
        "Pipeline",
        pipeline(
            "text-classification",
            model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
        ),
    )
