.PHONY: install dev test lint format type-check clean docker-build docker-up docker-down help

help:  ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-20s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install:  ## Install dependencies with Poetry
	poetry install

dev:  ## Run development server with auto-reload
	poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

test:  ## Run tests with coverage
	poetry run pytest --cov=app --cov-report=term-missing --cov-report=html

test-watch:  ## Run tests in watch mode
	poetry run pytest-watch

lint:  ## Run linting checks
	poetry run ruff check src/ tests/

format:  ## Format code with Ruff
	poetry run ruff format src/ tests/
	poetry run ruff check --fix src/ tests/

type-check:  ## Run type checking with Mypy
	poetry run mypy src/

quality:  ## Run all quality checks (lint, format-check, type-check, test)
	poetry run ruff check src/ tests/
	poetry run ruff format --check src/ tests/
	poetry run mypy src/
	poetry run pytest --cov=app

pre-commit-install:  ## Install pre-commit hooks
	poetry run pre-commit install

pre-commit:  ## Run pre-commit hooks on all files
	poetry run pre-commit run --all-files

clean:  ## Clean up generated files
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	rm -rf htmlcov/
	rm -f .coverage
	rm -f coverage.xml

docker-build:  ## Build Docker image
	docker build -t iykyk:latest .

docker-up:  ## Start Docker Compose services
	docker compose up -d

docker-down:  ## Stop Docker Compose services
	docker compose down

docker-logs:  ## View Docker Compose logs
	docker compose logs -f

docker-shell:  ## Open shell in running container
	docker compose exec web /bin/bash

setup:  ## Complete setup (install, pre-commit, and create .env)
	@make install
	@make pre-commit-install
	@if [ ! -f .env ]; then cp .env.example .env; echo "Created .env file from .env.example"; fi
	@echo "Setup complete! Run 'make dev' to start the development server."
