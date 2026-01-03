"""User schemas."""

from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    """Base user schema."""

    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50)
    full_name: str | None = None


class UserCreate(UserBase):
    """Schema for creating a user."""

    pass


class User(UserBase):
    """User schema with ID."""

    id: int

    model_config = {"from_attributes": True}
