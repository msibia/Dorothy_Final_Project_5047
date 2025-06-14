# Dorothy_Final_Project_5047
Final Project for AltSchool Python backend engineering class

# Event Management API System

## Project Structure

event_management_api/
├── main.py
├── requirements.txt
├── schemas/
│   └── data_models.py
├── routes/
│   ├── users.py
│   ├── events.py
│   ├── speakers.py
│   └── registrations.py
└── services/
    └── data_storage.py

## Setup Instructions

1. **Create the project directory structure:**
   ``` bash
   mkdir event_management_api
   cd event_management_api
   mkdir schemas routers services
   touch schemas/__init__.py routes/__init__.py services/__init__.py
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Run the application:**
    Using uvicorn directly:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

4. **Access the API:**
   - API Base URL: `http://localhost:8000`
   - Interactive Documentation: `http://localhost:8000/docs`
   - Alternative Documentation: `http://localhost:8000/redoc`

## API Endpoints

### Users
- `POST /api/v1/users/` - Create a new user
- `GET /api/v1/users/` - Get all users
- `GET /api/v1/users/{user_id}` - Get a specific user
- `PUT /api/v1/users/{user_id}` - Update a user
- `DELETE /api/v1/users/{user_id}` - Delete a user
- `PATCH /api/v1/users/{user_id}/deactivate` - Deactivate a user

### Events
- `POST /api/v1/events/` - Create a new event
- `GET /api/v1/events/` - Get all events
- `GET /api/v1/events/{event_id}` - Get a specific event
- `PUT /api/v1/events/{event_id}` - Update an event
- `DELETE /api/v1/events/{event_id}` - Delete an event
- `PATCH /api/v1/events/{event_id}/close` - Close event registration

### Speakers
- `POST /api/v1/speakers/` - Create a new speaker
- `GET /api/v1/speakers/` - Get all speakers
- `GET /api/v1/speakers/{speaker_id}` - Get a specific speaker
- `PUT /api/v1/speakers/{speaker_id}` - Update a speaker
- `DELETE /api/v1/speakers/{speaker_id}` - Delete a speaker

### Registrations
- `POST /api/v1/registrations/` - Register a user for an event
- `GET /api/v1/registrations/` - Get all registrations (with details)
- `GET /api/v1/registrations/{registration_id}` - Get a specific registration
- `GET /api/v1/registrations/user/{user_id}` - Get registrations for a user
- `PATCH /api/v1/registrations/{registration_id}/attend` - Mark attendance

## Features

**Complete CRUD operations** for all entities
**Validation rules** implemented:
- Only active users can register
- Users cannot register twice for the same event
- Events must be open for registration
**Proper HTTP status codes** for all operations
**Modular structure** with separate routes and services
**Pydantic models** for validation
**In-memory storage** using dictionaries
**Automatic API documentation** with FastAPI


