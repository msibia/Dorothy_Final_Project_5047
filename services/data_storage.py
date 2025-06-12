from datetime import datetime
from typing import Dict, List, Optional
from schemas.data_models import User, Event, Speaker, Registration

# In-memory data storage
users_db: Dict[int, User] = {}
events_db: Dict[int, Event] = {}
speakers_db: Dict[int, Speaker] = {}
registrations_db: Dict[int, Registration] = {}

# ID counters
user_id_counter = 0
event_id_counter = 0
speaker_id_counter = 0
registration_id_counter = 0

def get_next_user_id() -> int:
    global user_id_counter
    user_id_counter += 1
    return user_id_counter

def get_next_event_id() -> int:
    global event_id_counter
    event_id_counter += 1
    return event_id_counter

def get_next_speaker_id() -> int:
    global speaker_id_counter
    speaker_id_counter += 1
    return speaker_id_counter

def get_next_registration_id() -> int:
    global registration_id_counter
    registration_id_counter += 1
    return registration_id_counter

def initialize_speakers():
    """Initialize the app with 3 speakers"""
    speakers_data = [
        {"name": "Dr. Jimmy Moore", "topic": "An Analysis on the Relationship between Chemokine Gradients and T-Cell Migration"},
        {"name": "Dr. Oluseyi Ajayi", "topic": "The Role of Nanotechnology in Improving the Efficiency of Refrigeration Systems"},
        {"name": "Prof. Mfon Ekpo", "topic": "A Linguistic Analysis of Afrobeat Song - Laho"}
    ]
    
    for speaker_data in speakers_data:
        speaker_id = get_next_speaker_id()
        speaker = Speaker(
            id=speaker_id,
            name=speaker_data["name"],
            topic=speaker_data["topic"]
        )
        speakers_db[speaker_id] = speaker

# User operations
def create_user(user_data: dict) -> User:
    user_id = get_next_user_id()
    user = User(id=user_id, **user_data)
    users_db[user_id] = user
    return user

def get_user(user_id: int) -> Optional[User]:
    return users_db.get(user_id)

def get_all_users() -> List[User]:
    return list(users_db.values())

def update_user(user_id: int, user_data: dict) -> Optional[User]:
    if user_id in users_db:
        user = users_db[user_id]
        for key, value in user_data.items():
            if value is not None:
                setattr(user, key, value)
        return user
    return None

def delete_user(user_id: int) -> bool:
    if user_id in users_db:
        del users_db[user_id]
        return True
    return False

def deactivate_user(user_id: int) -> Optional[User]:
    if user_id in users_db:
        users_db[user_id].is_active = False
        return users_db[user_id]
    return None

# Event operations
def create_event(event_data: dict) -> Event:
    event_id = get_next_event_id()
    event = Event(id=event_id, **event_data)
    events_db[event_id] = event
    return event

def get_event(event_id: int) -> Optional[Event]:
    return events_db.get(event_id)

def get_all_events() -> List[Event]:
    return list(events_db.values())

def update_event(event_id: int, event_data: dict) -> Optional[Event]:
    if event_id in events_db:
        event = events_db[event_id]
        for key, value in event_data.items():
            if value is not None:
                setattr(event, key, value)
        return event
    return None

def delete_event(event_id: int) -> bool:
    if event_id in events_db:
        del events_db[event_id]
        return True
    return False

def close_event_registration(event_id: int) -> Optional[Event]:
    if event_id in events_db:
        events_db[event_id].is_open = False
        return events_db[event_id]
    return None

# Speaker operations
def create_speaker(speaker_data: dict) -> Speaker:
    speaker_id = get_next_speaker_id()
    speaker = Speaker(id=speaker_id, **speaker_data)
    speakers_db[speaker_id] = speaker
    return speaker

def get_speaker(speaker_id: int) -> Optional[Speaker]:
    return speakers_db.get(speaker_id)

def get_all_speakers() -> List[Speaker]:
    return list(speakers_db.values())

def update_speaker(speaker_id: int, speaker_data: dict) -> Optional[Speaker]:
    if speaker_id in speakers_db:
        speaker = speakers_db[speaker_id]
        for key, value in speaker_data.items():
            if value is not None:
                setattr(speaker, key, value)
        return speaker
    return None

def delete_speaker(speaker_id: int) -> bool:
    if speaker_id in speakers_db:
        del speakers_db[speaker_id]
        return True
    return False

# Registration operations
def create_registration(registration_data: dict) -> Registration:
    registration_id = get_next_registration_id()
    registration = Registration(
        id=registration_id,
        registration_date=datetime.now(),
        **registration_data
    )
    registrations_db[registration_id] = registration
    return registration

def get_registration(registration_id: int) -> Optional[Registration]:
    return registrations_db.get(registration_id)

def get_all_registrations() -> List[Registration]:
    return list(registrations_db.values())

def get_user_registrations(user_id: int) -> List[Registration]:
    return [reg for reg in registrations_db.values() if reg.user_id == user_id]

def get_event_registrations(event_id: int) -> List[Registration]:
    return [reg for reg in registrations_db.values() if reg.event_id == event_id]

def update_registration(registration_id: int, registration_data: dict) -> Optional[Registration]:
    if registration_id in registrations_db:
        registration = registrations_db[registration_id]
        for key, value in registration_data.items():
            if value is not None:
                setattr(registration, key, value)
        return registration
    return None

def user_already_registered(user_id: int, event_id: int) -> bool:
    return any(
        reg.user_id == user_id and reg.event_id == event_id 
        for reg in registrations_db.values()
    )

def mark_attendance(registration_id: int) -> Optional[Registration]:
    if registration_id in registrations_db:
        registrations_db[registration_id].attended = True
        return registrations_db[registration_id]
    return None