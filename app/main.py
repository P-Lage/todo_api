from fastapi import FastAPI
from app import models, database, crud
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import TaskCreate, Task, TaskUpdate
from fastapi import HTTPException

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def root():
    return {"message": "API To-Do está no ar!"}

@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate):
    return crud.create_task(task)

@app.get("/tasks/", response_model=list[Task])
def read_tasks():
    return crud.get_tasks()

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    return crud.delete_task(task_id)

@app.patch("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_data: TaskUpdate):
    task = crud.update_task(task_id, task_data)
    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return task
