from pydantic import BaseModel
from datetime import datetime

class TaskCreate(BaseModel):
    title: str
    completed: bool = False
    due_date: datetime | None = None

class Task(TaskCreate):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class TaskUpdate(BaseModel):
    title: str | None = None
    completed: bool | None = None
