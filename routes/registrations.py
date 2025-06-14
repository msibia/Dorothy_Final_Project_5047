from fastapi import APIRouter, HTTPException, status
from typing import List
from schemas.data_models import Registration, RegistrationCreate, RegistrationWithDetails
from services import data_storage

router = APIRouter()

@router.post("/", response_model=Registration, status_code=status.HTTP_201_CREATED)
async def register_user_for_event(registration: RegistrationCreate):
    """Register a user for an event"""
    # Check if user exists and is active
    user = data_storage.get_user(registration.user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only active users can register for events"
        )
    
    # Check if event exists and is open
    event = data_storage.get_event(registration.event_id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found"
        )
    
    if not event.is_open:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Event registration is closed"
        )
    
    # Check if user is already registered for this event
    if data_storage.user_already_registered(registration.user_id, registration.event_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User is already registered for this event"
        )
    
    # Create registration
    registration_data = registration.model_dump()
    created_registration = data_storage.create_registration(registration_data)
    return created_registration

@router.get("/", response_model=List[RegistrationWithDetails])
async def get_all_registrations():
    """Get all registrations with user and event details"""
    registrations = data_storage.get_all_registrations()
    detailed_registrations = []
    
    for reg in registrations:
        user = data_storage.get_user(reg.user_id)
        event = data_storage.get_event(reg.event_id)
        
        if user and event:
            detailed_reg = RegistrationWithDetails(
                id=reg.id,
                user_id=reg.user_id,
                event_id=reg.event_id,
                registration_date=reg.registration_date,
                attended=reg.attended,
                user_name=user.name,
                user_email=user.email,
                event_title=event.title,
                event_location=event.location,
                event_date=event.date
            )
            detailed_registrations.append(detailed_reg)
    
    return detailed_registrations

@router.get("/{registration_id}", response_model=Registration)
async def get_registration(registration_id: int):
    """Get a specific registration by ID"""
    registration = data_storage.get_registration(registration_id)
    if not registration:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Registration not found"
        )
    return registration

@router.get("/user/{user_id}", response_model=List[RegistrationWithDetails])
async def get_user_registrations(user_id: int):
    """Get all registrations for a specific user"""
    user = data_storage.get_user(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    registrations = data_storage.get_user_registrations(user_id)
    detailed_registrations = []
    
    for reg in registrations:
        event = data_storage.get_event(reg.event_id)
        if event:
            detailed_reg = RegistrationWithDetails(
                id=reg.id,
                user_id=reg.user_id,
                event_id=reg.event_id,
                registration_date=reg.registration_date,
                attended=reg.attended,
                user_name=user.name,
                user_email=user.email,
                event_title=event.title,
                event_location=event.location,
                event_date=event.date
            )
            detailed_registrations.append(detailed_reg)
    
    return detailed_registrations

@router.patch("/{registration_id}/attend", response_model=Registration)
async def mark_attendance(registration_id: int):
    """Mark attendance for a registration (set attended to True)"""
    registration = data_storage.mark_attendance(registration_id)
    if not registration:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Registration not found"
        )
    return registration