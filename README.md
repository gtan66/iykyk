# IYKYK

A modern Python web application built with FastAPI and best practices for production-ready applications.

## Features

- **FastAPI** - Modern, fast web framework with automatic API documentation
- **Type Safety** - Full type hints with Mypy strict mode
- **Code Quality** - Ruff for linting and formatting
- **Testing** - Pytest with async support and coverage reporting
- **Pre-commit Hooks** - Automated code quality checks
- **Docker** - Production-ready containerization
- **CI/CD** - GitHub Actions for automated testing and deployment
- **Dependency Management** - UV for blazing-fast package management
- **Security** - Best practices including non-root Docker user, security scanning

## Project Structure

```
iykyk/
├── src/
│   └── app/
│       ├── api/           # API route handlers
│       ├── models/        # Database models
│       ├── schemas/       # Pydantic schemas
│       ├── config.py      # Application configuration
│       └── main.py        # FastAPI application
├── tests/                 # Test files
├── .github/
│   └── workflows/         # CI/CD workflows
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose setup
├── pyproject.toml         # Project dependencies and tool config
└── README.md
```

## Requirements

- Python 3.11+
- UV (for dependency management)
- Docker (optional, for containerization)

## Quick Start

### 1. Clone the repository

```bash
git clone <repository-url>
cd iykyk
```

### 2. Install dependencies with UV

```bash
# Install UV if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install project dependencies
uv sync
```

### 3. Set up environment variables

```bash
cp .env.example .env
# Edit .env with your configuration
```

### 4. Run the application

```bash
# Development mode with auto-reload
uv run uvicorn app.main:app --reload

# Or use the Makefile
make dev
```

The API will be available at:
- Application: http://localhost:8000
- Interactive API docs: http://localhost:8000/docs
- Alternative API docs: http://localhost:8000/redoc

## Development

### Running Tests

```bash
# Run all tests with coverage
uv run pytest

# Run with verbose output
uv run pytest -v

# Run specific test file
uv run pytest tests/test_users.py
```

### Code Quality

```bash
# Lint with Ruff
uv run ruff check src/ tests/

# Format code with Ruff
uv run ruff format src/ tests/

# Type check with Mypy
uv run mypy src/
```

### Pre-commit Hooks

```bash
# Install pre-commit hooks
uv run pre-commit install

# Run hooks manually
uv run pre-commit run --all-files
```

## Docker

### Build and run with Docker

```bash
# Build the image
docker build -t iykyk .

# Run the container
docker run -p 8000:8000 iykyk
```

### Using Docker Compose

```bash
# Start all services
docker compose up

# Start in detached mode
docker compose up -d

# View logs
docker compose logs -f

# Stop services
docker compose down
```

## API Documentation

Once the application is running, visit:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Available Endpoints

#### Health Checks
- `GET /health` - Health check endpoint
- `GET /ready` - Readiness check endpoint

#### Users API
- `GET /api/v1/users/` - List all users
- `GET /api/v1/users/{user_id}` - Get a specific user
- `POST /api/v1/users/` - Create a new user
- `DELETE /api/v1/users/{user_id}` - Delete a user

## Configuration

Configuration is managed through environment variables and the `app/config.py` file using Pydantic Settings.

Key configuration options:

- `PROJECT_NAME` - Application name
- `VERSION` - Application version
- `DEBUG` - Debug mode (True/False)
- `DATABASE_URL` - Database connection string
- `SECRET_KEY` - Secret key for security features
- `ALLOWED_ORIGINS` - CORS allowed origins

## Deployment

### Environment Variables

For production deployment, ensure you set:

```bash
DEBUG=False
SECRET_KEY=<strong-random-key>
DATABASE_URL=<production-database-url>
ALLOWED_ORIGINS=["https://yourdomain.com"]
```

### Docker Deployment

The included Dockerfile uses multi-stage builds for optimized image size and includes:

- Non-root user for security
- Health checks
- Proper Python optimization flags
- Minimal production dependencies

## Testing

The project uses Pytest with the following features:

- Async test support (`pytest-asyncio`)
- Coverage reporting (`pytest-cov`)
- Test client for API testing (`TestClient` from FastAPI)

Run tests with coverage:

```bash
uv run pytest --cov=app --cov-report=html
```

View coverage report:

```bash
open htmlcov/index.html
```

## Code Quality Tools

### Ruff

Fast Python linter and formatter that replaces Black, isort, and Flake8:

- Automatic import sorting
- Code formatting
- PEP 8 compliance
- Additional linting rules

### Mypy

Static type checker with strict mode enabled:

- Ensures type safety
- Catches type-related bugs early
- Improves code documentation

### Pre-commit

Automated checks before each commit:

- Trailing whitespace removal
- YAML/JSON validation
- Ruff linting and formatting
- Mypy type checking

## CI/CD

GitHub Actions workflows include:

1. **Lint and Test** - Runs on multiple Python versions
   - Code linting with Ruff
   - Type checking with Mypy
   - Unit tests with Pytest
   - Coverage reporting

2. **Docker Build** - Validates Docker image builds

3. **Security** - Scans for vulnerabilities with Trivy

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and linting (`make quality` or `uv run pytest && uv run ruff check .`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## License

This project is licensed under the MIT License.

## Best Practices Implemented

- **Type Safety**: Full type hints throughout the codebase
- **Dependency Injection**: FastAPI's dependency injection for clean architecture
- **Configuration Management**: Environment-based configuration with Pydantic
- **Testing**: Comprehensive test coverage with pytest
- **Code Quality**: Automated linting and formatting
- **Security**: Non-root Docker user, security scanning, secret management
- **Documentation**: Auto-generated API docs, comprehensive README
- **CI/CD**: Automated testing and deployment pipelines
- **Error Handling**: Proper HTTP exception handling
- **CORS**: Configurable CORS middleware
- **Logging**: Structured logging (ready to be extended)
- **Health Checks**: Kubernetes-ready health and readiness endpoints
