import argparse
from unittest.mock import MagicMock, patch

from analyzer.__main__ import cli


@patch("analyzer.__main__.create_app_production")
@patch("analyzer.__main__.uvicorn.run")
def test_cli(mock_uvicorn_run: MagicMock, mock_create_app: MagicMock) -> None:
    with patch(
        "argparse.ArgumentParser.parse_args",
        return_value=argparse.Namespace(serve=True),
    ):
        cli()
        mock_uvicorn_run.assert_called_once_with(
            mock_create_app(),
            host="localhost",
            port=8008,
        )


def test_cli_serve_false() -> None:
    with patch(
        "argparse.ArgumentParser.parse_args",
        return_value=argparse.Namespace(serve=False),
    ):
        cli()
