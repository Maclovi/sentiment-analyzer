from collections.abc import Callable
from typing import TypeAlias

from analyzer.usecases import interfaces

Pipeline: TypeAlias = Callable[[str], list[interfaces.AnalyzeOutput]]
