# Sentiment Analyzer

Sentiment Analyzer is a tool designed to automatically detect the emotional tone of text messages. It analyzes input text and classifies it as either positive or negative based on word choice and emotional context.

## Features

- **Sentiment Analysis:** Classifies text as positive or negative.
- **GraphQL API:** Provides a GraphQL endpoint for interacting with the analyzer.
- **REST API:** Provides a REST endpoint for health checks and sentiment analysis.
- **Docker Support:** Comes with a `docker-compose` setup for easy deployment.

## Getting Started

To get started with the Sentiment Analyzer, you'll need to have Python 3.10 or higher and `just` and `uv` installed.

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Maclovi/sentiment-analyzer.git
    cd sentiment-analyzer
    ```

2.  **Create virtual environment:**

    This command will create a virtual environment.

    ```bash
    uv venv
    ```

3.  **Bootstrap the project:**

    This command will install all the necessary dependencies, and set up pre-commit hooks.

    ```bash
    just bootstrap
    ```

## Usage

To run the Sentiment Analyzer server, use the following command:

```bash
just serve
```

The application will be available at `http://localhost:8008`.

## Running Tests

To run the test suite, use the following command:

```bash
just test
```

To run the tests with coverage, use:

```bash
just test-cov
```

## Linting and Static Analysis

To check the code for style and potential errors, you can use the following commands:

- **Linting:**

  ```bash
  just lint
  ```

- **Static Analysis:**

  ```bash
  just static
  ```

- **Pre-commit Hooks:**

  ```bash
  just pre-commit
  ```

## Docker

The project includes a `docker-compose.yml` file for running the application in Docker containers.

- **Start the containers:**

  ```bash
  just up
  ```

- **Stop the containers:**

  ```bash
  just down
  ```

## Dependencies

The main dependencies of the project are:

- **FastAPI:** A modern, fast (high-performance) web framework for building APIs with Python 3.10+ based on standard Python type hints.
- **Uvicorn:** A lightning-fast ASGI server implementation, using uvloop and httptools.
- **Strawberry-GraphQL:** A Python GraphQL library that uses type hints to create a schema-first API.
- **Dishka:** A dependency injection framework for Python.
- **Transformers:** A state-of-the-art machine learning library for PyTorch, TensorFlow, and JAX.

For a full list of dependencies, please see the `pyproject.toml` file.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
