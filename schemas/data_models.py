from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from uuid import UUID


# User Schemas
class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None

class User(UserBase):
    id: UUID
    is_active: bool = True

    class Config:
        from_attributes = True

# Event Schemas
class EventBase(BaseModel):
    title: str
    location: str
    date: datetime

class Event(EventBase):
    id: UUID
    is_open: bool = True

    class Config:
        from_attributes = True

class EventCreate(EventBase):
    pass

class EventUpdate(BaseModel):
    title: Optional[str] = None
    location: Optional[str] = None
    date: Optional[datetime] = None
    is_open: Optional[bool] = None

# Speaker Schemas
class SpeakerBase(BaseModel):
    name: str
    topic: str

class SpeakerCreate(SpeakerBase):
    pass

class SpeakerUpdate(BaseModel):
    name: Optional[str] = None
    topic: Optional[str] = None

class Speaker(SpeakerBase):
    id: UUID

    class Config:
        from_attributes = True

# Registration Schemas
class RegistrationBase(BaseModel):
    user_id: int
    event_id: int

class RegistrationCreate(RegistrationBase):
    pass

class RegistrationUpdate(BaseModel):
    attended: Optional[bool] = None

class Registration(RegistrationBase):
    id: UUID
    registration_date: datetime
    attended: bool = False

    class Config:
        from_attributes = True

# Response Schemas
class RegistrationWithDetails(Registration):
    user_name: str
    user_email: str
    event_title: str
    event_location: str
    event_date: datetime

    