"""Main FastAPI application module."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import health, users
from app.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="A modern Python web application with best practices",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router, tags=["health"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])


@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint."""
    return {"message": "Welcome to IYKYK API", "version": settings.VERSION}
