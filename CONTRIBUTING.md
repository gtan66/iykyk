# Contributing to IYKYK

Thank you for your interest in contributing to IYKYK! This document provides guidelines and instructions for contributing.

## Code of Conduct

Be respectful and constructive in all interactions.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/iykyk.git`
3. Create a new branch: `git checkout -b feature/your-feature-name`
4. Set up your development environment:
   ```bash
   make setup
   ```

## Development Workflow

### 1. Set Up Your Environment

```bash
# Install dependencies
uv sync

# Install pre-commit hooks
uv run pre-commit install

# Copy environment file
cp .env.example .env
```

### 2. Make Your Changes

- Write clear, concise code
- Follow the existing code style
- Add tests for new features
- Update documentation as needed

### 3. Run Quality Checks

Before committing, ensure all checks pass:

```bash
# Run all quality checks
make quality

# Or run individually:
make lint        # Linting
make type-check  # Type checking
make test        # Tests
```

### 4. Commit Your Changes

We use conventional commits for clear commit messages:

```bash
# Format: <type>(<scope>): <description>

git commit -m "feat(api): add user authentication endpoint"
git commit -m "fix(users): resolve duplicate email validation"
git commit -m "docs(readme): update installation instructions"
```

Common types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### 5. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub.

## Code Style Guidelines

### Python Code Style

We use Ruff for linting and formatting:

- Line length: 100 characters
- Follow PEP 8 conventions
- Use type hints for all functions
- Write docstrings for public functions and classes

Example:

```python
def create_user(username: str, email: str) -> User:
    """Create a new user with the given username and email.

    Args:
        username: The desired username
        email: The user's email address

    Returns:
        The created User object

    Raises:
        ValueError: If username or email is invalid
    """
    # Implementation
```

### Type Hints

- Always use type hints for function parameters and return values
- Use modern type hint syntax (e.g., `list[str]` instead of `List[str]`)
- Enable strict type checking with Mypy

### Testing

- Write tests for all new features
- Maintain or improve code coverage
- Use descriptive test names
- Follow the Arrange-Act-Assert pattern

Example:

```python
def test_create_user_with_valid_data(client: TestClient) -> None:
    """Test creating a user with valid data returns 201."""
    # Arrange
    user_data = {"username": "testuser", "email": "test@example.com"}

    # Act
    response = client.post("/api/v1/users/", json=user_data)

    # Assert
    assert response.status_code == 201
    assert response.json()["username"] == user_data["username"]
```

## Pull Request Guidelines

### Before Submitting

- [ ] All tests pass
- [ ] Code is properly formatted
- [ ] Type checking passes
- [ ] Documentation is updated
- [ ] Commit messages follow conventional commits
- [ ] Branch is up to date with main

### PR Description

Include in your PR description:

1. **What**: Brief description of changes
2. **Why**: Reason for the changes
3. **How**: Implementation approach (if complex)
4. **Testing**: How you tested the changes
5. **Screenshots**: If UI changes (not applicable for API)

Example:

```markdown
## What
Add user authentication with JWT tokens

## Why
Users need secure authentication to access protected endpoints

## How
- Implemented JWT token generation and validation
- Added login and refresh token endpoints
- Created authentication middleware

## Testing
- Added unit tests for token generation/validation
- Tested login flow with test client
- Verified protected endpoints require valid tokens
```

### Review Process

1. Automated checks must pass (CI/CD)
2. At least one maintainer approval required
3. Address review comments promptly
4. Keep discussions respectful and constructive

## Project Structure

```
src/app/
├── api/           # API route handlers
├── models/        # Database models
├── schemas/       # Pydantic schemas
├── config.py      # Configuration
└── main.py        # Application entry point
```

When adding new features:

- API endpoints go in `src/app/api/`
- Database models go in `src/app/models/`
- Request/response schemas go in `src/app/schemas/`
- Tests go in `tests/` matching the source structure

## Reporting Issues

When reporting bugs, include:

1. Description of the issue
2. Steps to reproduce
3. Expected behavior
4. Actual behavior
5. Environment details (Python version, OS, etc.)
6. Error messages and logs

## Questions?

Feel free to open an issue for questions or join our discussions.

Thank you for contributing!
