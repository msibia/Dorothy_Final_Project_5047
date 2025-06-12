from fastapi import APIRouter, HTTPException, status
from typing import List
from schemas.data_models import User, UserCreate, UserUpdate
from services import data_storage

router = APIRouter()

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    """Create a new user"""
    user_data = user.model_dump()
    created_user = data_storage.create_user(user_data)
    return created_user

@router.get("/", response_model=List[User])
async def get_all_users():
    """Get all users"""
    return data_storage.get_all_users()

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    """Get a specific user by ID"""
    user = data_storage.get_user(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user_update: UserUpdate):
    """Update a user"""
    existing_user = data_storage.get_user(user_id)
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    update_data = user_update.model_dump(exclude_unset=True)
    updated_user = data_storage.update_user(user_id, update_data)
    return updated_user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    """Delete a user"""
    success = data_storage.delete_user(user_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

@router.patch("/{user_id}/deactivate", response_model=User)
async def deactivate_user(user_id: int):
    """Deactivate a user (set is_active to False)"""
    user = data_storage.deactivate_user(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user