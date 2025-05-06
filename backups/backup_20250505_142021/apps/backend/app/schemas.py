from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from enum import Enum

class ProjectStatus(str, Enum):
    PLANNED = "planned"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ON_HOLD = "on_hold"

class ClientBase(BaseModel):
    name: str
    contact_info: str
    address: str
    email: EmailStr
    phone: str
    status: bool = True

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class ProjectBase(BaseModel):
    client_id: int
    name: str
    description: str
    start_date: datetime
    end_date: datetime
    status: ProjectStatus
    location: str
    total_area: float
    project_type: str
    budget: float
    notes: Optional[str] = None

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True 