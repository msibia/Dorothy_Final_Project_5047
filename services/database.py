from datetime import datetime
from typing import Dict, List, Optional
from schemas.data_models import User, Event, Speaker, Registration

# In-memory data storage
users_db: Dict[int, User] = {}
events_db: Dict[int, Event] = {}
speakers_db: Dict[int, Speaker] = {}
registrations_db: Dict[int, Registration] = {}