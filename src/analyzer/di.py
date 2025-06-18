from collections.abc import Iterable

from dishka import Provider, Scope

from analyzer.infrastructure.neural.adapters import PipelineAdapter
from analyzer.infrastructure.neural.provider import create_pipeline
from analyzer.usecases import interfaces
from analyzer.usecases.interactors import SentimentAnalyzerHandler


def neural_provider() -> Provider:
    provider = Provider(scope=Scope.APP)
    provider.provide(create_pipeline)
    provider.provide(PipelineAdapter, provides=interfaces.SentimentNeural)
    return provider


def interactors_provider() -> Provider:
    provider = Provider()
    provider.provide(SentimentAnalyzerHandler, scope=Scope.APP)
    return provider


def setup_all_providers() -> Iterable[Provider]:
    return (
        neural_provider(),
        interactors_provider(),
    )
