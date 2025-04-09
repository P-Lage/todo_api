from app import models, schemas, database

def create_task(task: schemas.TaskCreate):
    db = database.SessionLocal()
    db_task = models.Task(title=task.title, completed=task.completed)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    db.close()
    return db_task

def get_tasks():
    db = database.SessionLocal()
    tasks = db.query(models.Task).all()
    db.close()
    return tasks

def delete_task(task_id: int):
    db = database.SessionLocal()
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    db.close()
    return {"deleted": task_id}

def update_task(task_id: int, task_data: schemas.TaskUpdate):
    db = database.SessionLocal()
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        db.close()
        return None

    if task_data.title is not None:
        task.title = task_data.title
    if task_data.completed is not None:
        task.completed = task_data.completed

    db.commit()
    db.refresh(task)
    db.close()
    return task
