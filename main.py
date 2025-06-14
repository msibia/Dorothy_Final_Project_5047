from contextlib import asynccontextmanager
from fastapi import FastAPI
from routes import users, events, registrations, speakers
from services.data_storage import initialize_speakers

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    try:
        initialize_speakers()
        print("Speakers initialized successfully")
    except Exception as e:
        print(f"Error initializing speakers: {e}")
        raise
    yield
    # Shutdown (if needed)

app = FastAPI(
    title="Event Management API",
    description="A comprehensive event management system with user registration, event tracking, and speaker management",
    version="1.0.0",
    lifespan=lifespan
)

# Include routes
app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(events.router, prefix="/api/v1/events", tags=["Events"])
app.include_router(speakers.router, prefix="/api/v1/speakers", tags=["Speakers"])
app.include_router(registrations.router, prefix="/api/v1/registrations", tags=["Registrations"])

@app.get("/")
async def root():
    return {"message": "Welcome to Event Management API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)