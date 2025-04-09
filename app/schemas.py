from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    completed: bool = False

class Task(TaskCreate):
    id: int

    class Config:
        orm_mode = True

class TaskUpdate(BaseModel):
    title: str | None = None
    completed: bool | None = None
