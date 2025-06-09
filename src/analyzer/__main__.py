import argparse

import uvicorn

from analyzer.web import create_app_production


def cli() -> None:
    parser = argparse.ArgumentParser(
        prog="snetiment-analyzer",
        description="CLI sentiment-analyzer",
    )
    parser.add_argument("-s", "--serve", action="store_true")
    args = parser.parse_args()

    if args.serve:
        uvicorn.run(create_app_production())


if __name__ == "__main__":
    cli()
