"""User endpoints."""

from fastapi import APIRouter, HTTPException, status

from app.schemas.user import User, UserCreate

router = APIRouter()

# In-memory storage for demo purposes
users_db: dict[int, User] = {}
next_id = 1


@router.get("/", response_model=list[User])
async def list_users() -> list[User]:
    """List all users."""
    return list(users_db.values())


@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int) -> User:
    """Get a user by ID."""
    if user_id not in users_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {user_id} not found",
        )
    return users_db[user_id]


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate) -> User:
    """Create a new user."""
    global next_id
    new_user = User(id=next_id, **user.model_dump())
    users_db[next_id] = new_user
    next_id += 1
    return new_user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int) -> None:
    """Delete a user."""
    if user_id not in users_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {user_id} not found",
        )
    del users_db[user_id]
