from fastapi import APIRouter, HTTPException, status
from typing import List
from uuid import UUID
from schemas.data_models import Event, EventCreate, EventUpdate
from services import data_storage

router = APIRouter()

@router.post("/", response_model=Event, status_code=status.HTTP_201_CREATED)
async def create_event(event: EventCreate):
    """Create a new event"""
    event_data = event.model_dump()
    created_event = data_storage.create_event(event_data)
    return created_event

@router.get("/", response_model=List[Event])
async def get_all_events():
    """Get all events"""
    return data_storage.get_all_events()

@router.get("/{event_id}", response_model=Event)
async def get_event(event_id: UUID):
    """Get a specific event by ID"""
    event = data_storage.get_event(event_id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found"
        )
    return event

@router.put("/{event_id}", response_model=Event)
async def update_event(event_id: UUID, event_update: EventUpdate):
    """Update an event"""
    existing_event = data_storage.get_event(event_id)
    if not existing_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found"
        )
    
    update_data = event_update.model_dump(exclude_unset=True)
    updated_event = data_storage.update_event(event_id, update_data)
    return updated_event

@router.delete("/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_event(event_id: UUID):
    """Delete an event"""
    success = data_storage.delete_event(event_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found"
        )

@router.patch("/{event_id}/close", response_model=Event)
async def close_event_registration(event_id: UUID):
    """Close event registration (set is_open to False)"""
    event = data_storage.close_event_registration(event_id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found"
        )
    return event