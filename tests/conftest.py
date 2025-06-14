from collections.abc import Iterator
from unittest.mock import MagicMock, patch

import pytest

from analyzer.infrastructure.neural import PipelineAdapter


@pytest.fixture
def pipeline_neural_fake() -> Iterator[PipelineAdapter]:
    with patch("analyzer.infrastructure.neural.pipeline") as mock_pipeline:
        mock_pipe = MagicMock()
        mock_pipe.return_value = [{"label": "POSITIVE", "score": 0.9}]
        mock_pipeline.return_value = mock_pipe
        yield PipelineAdapter()
