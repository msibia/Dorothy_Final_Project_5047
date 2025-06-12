from fastapi import APIRouter, HTTPException, status
from typing import List
from schemas.data_models import Speaker, SpeakerCreate, SpeakerUpdate
from services import data_storage

router = APIRouter()

@router.post("/", response_model=Speaker, status_code=status.HTTP_201_CREATED)
async def create_speaker(speaker: SpeakerCreate):
    """Create a new speaker"""
    speaker_data = speaker.model_dump()
    created_speaker = data_storage.create_speaker(speaker_data)
    return created_speaker

@router.get("/", response_model=List[Speaker])
async def get_all_speakers():
    """Get all speakers"""
    return data_storage.get_all_speakers()

@router.get("/{speaker_id}", response_model=Speaker)
async def get_speaker(speaker_id: int):
    """Get a specific speaker by ID"""
    speaker = data_storage.get_speaker(speaker_id)
    if not speaker:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Speaker not found"
        )
    return speaker

@router.put("/{speaker_id}", response_model=Speaker)
async def update_speaker(speaker_id: int, speaker_update: SpeakerUpdate):
    """Update a speaker"""
    existing_speaker = data_storage.get_speaker(speaker_id)
    if not existing_speaker:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Speaker not found"
        )
    
    update_data = speaker_update.model_dump(exclude_unset=True)
    updated_speaker = data_storage.update_speaker(speaker_id, update_data)
    return updated_speaker

@router.delete("/{speaker_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_speaker(speaker_id: int):
    """Delete a speaker"""
    success = data_storage.delete_speaker(speaker_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Speaker not found"
        )
    return {"message": "Speaker deleted successfully"}