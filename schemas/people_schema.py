from pydantic import BaseModel, Field
from uuid import UUID

class BaseUser(BaseModel):
    id: UUID
    name: str

class User(BaseUser):
    email: str
    is_active: bool = Field(default=True)
 
 
class speaker(BaseUser):
    topic: str

    