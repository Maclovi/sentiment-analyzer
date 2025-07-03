# Sentiment Analyzer

A modern, high-performance sentiment analysis tool that automatically detects the emotional tone of text messages. Built with FastAPI and powered by state-of-the-art transformer models, it provides both REST and GraphQL APIs for seamless integration.

## 🚀 Features

- **High-Performance Sentiment Analysis**: Classifies text as positive or negative using DistilBERT model
- **Dual API Support**: Choose between REST and GraphQL endpoints
- **Production Ready**: Docker support with nginx reverse proxy
- **Type Safe**: Built with Python type hints and modern development practices
- **Comprehensive Testing**: Full test coverage with pytest
- **Development Tools**: Pre-commit hooks, linting, and static analysis

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.10+** (3.10, 3.11, 3.12, or 3.13)
- **[uv](https://docs.astral.sh/uv/)** - Fast Python package manager
- **[just](https://github.com/casey/just)** - Command runner
- **Docker & Docker Compose** (optional, for containerized deployment)

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Maclovi/sentiment-analyzer.git
cd sentiment-analyzer
```

### 2. Set Up Development Environment

```bash
# Create virtual environment
uv venv
# activate virtual via source .venv/bin/activate

# Bootstrap the project (installs dependencies and sets up pre-commit hooks)
just bootstrap
```

This will:

- Copy `.env.dist` to `.env` for configuration
- Install all dependencies including development tools
- Set up pre-commit hooks for code quality

### 3. Manual Installation (Alternative)

If you prefer manual setup:

```bash
# Create and activate virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv pip install -e ".[dev,ai]"

# Install pre-commit hooks
pre-commit install
```

## 🏃 Quick Start

### Start the Development Server

```bash
just serve
```

The application will be available at `http://localhost:8008`

### API Endpoints

#### REST API

**Health Check:**

```bash
curl http://localhost:8008/v1/healthcheck
```

**Sentiment Analysis:**

```bash
curl -X POST http://localhost:8008/v1/sentiment \
  -H "Content-Type: application/json" \
  -d '{"text": "I love this product!"}'
```

Response:

```json
{
  "label": "POSITIVE",
  "score": 0.9998
}
```

#### GraphQL API

Access the GraphQL playground at `http://localhost:8008/v1/graphql`

**Health Check Query:**

```graphql
query {
  healthcheck
}
```

**Sentiment Analysis Mutation:**

```graphql
mutation {
  sentimentText(data: { text: "This is amazing!" }) {
    label
    score
  }
}
```

## 🐳 Docker Deployment

### Quick Start with Docker

```bash
# Start all services (API + nginx)
just up

# Access the application
curl http://localhost/api/v1/healthcheck
```

### Stop Services

```bash
just down
```

### Docker Architecture

The Docker setup includes:

- **API Service**: FastAPI application with sentiment analysis
- **Nginx**: Reverse proxy for production-ready deployment
- **Health Checks**: Automatic service health monitoring

## 🧪 Development

### Running Tests

```bash
# Run all tests
just test

# Run tests with coverage report
just test-cov

# Run specific test file
just test tests/test_endpoints.py
```

### Code Quality

```bash
# Run linting (ruff, codespell)
just lint

# Run static analysis (mypy, bandit, semgrep)
just static

# Run all pre-commit hooks
just pre-commit
```

### Development Workflow

1. **Make changes** to your code
2. **Run tests** with `just test`
3. **Check code quality** with `just lint` and `just static`
4. **Commit changes** (pre-commit hooks will run automatically)

## 📖 API Documentation

### REST API

| Endpoint          | Method | Description               |
| ----------------- | ------ | ------------------------- |
| `/v1/healthcheck` | GET    | Health check endpoint     |
| `/v1/sentiment`   | POST   | Analyze sentiment of text |

### GraphQL API

| Operation       | Type     | Description               |
| --------------- | -------- | ------------------------- |
| `healthcheck`   | Query    | Health check query        |
| `sentimentText` | Mutation | Analyze sentiment of text |

### Request/Response Examples

**REST Request:**

```json
{
  "text": "I'm having a great day!"
}
```

**Response:**

```json
{
  "label": "POSITIVE",
  "score": 0.9995
}
```

**GraphQL Request:**

```graphql
mutation AnalyzeSentiment($text: String!) {
  sentimentText(data: { text: $text }) {
    label
    score
  }
}
```

## 🏗️ Architecture

### Project Structure

```
src/analyzer/
├── __init__.py              # Package version
├── __main__.py              # Application entry point
├── bootstrap.py             # Configuration and routing setup
├── di.py                    # Dependency injection setup
├── web.py                   # FastAPI application factory
├── infrastructure/
│   ├── configs.py           # Configuration classes
│   └── neural/              # AI/ML components
│       ├── adapters.py      # ML model adapters
│       ├── annotations.py   # Type annotations
│       └── provider.py      # Model provider
├── presentation/
│   └── v1/                  # API v1 endpoints
│       ├── graphql/         # GraphQL schema and resolvers
│       └── routes/          # REST API routes
└── usecases/
    ├── interfaces.py        # Business logic interfaces
    └── interactors.py       # Business logic implementation
```

### Key Components

- **Clean Architecture**: Separation of concerns with clear boundaries
- **Dependency Injection**: Using Dishka for IoC container
- **Type Safety**: Full type hints with mypy validation
- **Modern Python**: Using dataclasses, protocols, and modern patterns

## 🔧 Configuration

### Environment Variables

Copy `.env.dist` to `.env` and configure:

```bash
# Server Configuration
ANALYZER_UVICORN_HOST=0.0.0.0
ANALYZER_UVICORN_PORT=8008
```

### Model Configuration

The application uses DistilBERT for sentiment analysis:

- **Model**: `distilbert/distilbert-base-uncased-finetuned-sst-2-english`
- **Task**: Text classification (sentiment analysis)
- **Labels**: POSITIVE, NEGATIVE
- **Score**: Confidence score (0.0 to 1.0)

## 🛠️ Available Commands

Run `just` to see all available commands:

```bash
just                    # Show all commands
just bootstrap         # Set up development environment
just serve             # Start development server
just test              # Run tests
just test-cov          # Run tests with coverage
just lint              # Run linting
just static            # Run static analysis
just pre-commit        # Run pre-commit hooks
just up                # Start Docker containers
just down              # Stop Docker containers
```

## 📦 Dependencies

### Core Dependencies

- **FastAPI**: Modern web framework for APIs
- **Uvicorn**: ASGI server with uvloop for high performance
- **Transformers**: Hugging Face transformers for ML models
- **Strawberry-GraphQL**: GraphQL library for Python
- **Dishka**: Dependency injection framework

### Development Dependencies

- **pytest**: Testing framework
- **ruff**: Fast Python linter and formatter
- **mypy**: Static type checker
- **bandit**: Security linter
- **pre-commit**: Git hooks for code quality

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and quality checks (`just test && just lint && just static`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Development Guidelines

- Follow the existing code style
- Add tests for new functionality
- Update documentation as needed
- Ensure all quality checks pass

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙋 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/Maclovi/sentiment-analyzer/issues) page
2. Create a new issue with detailed information
3. For general questions, use the discussion feature

## 🔮 Roadmap

- [ ] Support for additional languages
- [ ] Batch processing endpoints
- [ ] Model fine-tuning capabilities
- [ ] Real-time streaming analysis
- [ ] Advanced sentiment categories (neutral, mixed)
- [ ] Performance metrics and monitoring

---

Made with ❤️ by [Sergey Yavorsky](https://github.com/Maclovi)
