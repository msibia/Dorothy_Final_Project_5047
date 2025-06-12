from contextlib import asynccontextmanager
from fastapi import FastAPI
from routers import users, events, registrations, speakers
from services.data_storage import initialize_speakers


app = FastAPI()

# Include routers
app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(events.router, prefix="/api/v1/events", tags=["Events"])
app.include_router(speakers.router, prefix="/api/v1/speakers", tags=["Speakers"])
app.include_router(registrations.router, prefix="/api/v1/registrations", tags=["Registrations"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Event Management API"}

