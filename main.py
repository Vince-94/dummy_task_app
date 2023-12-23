from typing import List

from fastapi import FastAPI, HTTPException
from mangum import Mangum
from pydantic import BaseModel


app = FastAPI()


# Dummy data (in-memory database)
tasks = [
    {"id": 1, "title": "Task 1", "description": "This is task 1", "status": "incomplete"},
    {"id": 2, "title": "Task 2", "description": "This is task 2", "status": "complete"},
]


# Model for a Task
class Task(BaseModel):
    id: int
    title: str
    description: str
    status: str


# Get all tasks
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

# Get a specific task by ID
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Create a new task
@app.post("/tasks", response_model=dict, status_code=201)
def create_task(task: Task):
    new_task = {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "status": task.status,
    }
    tasks.append(new_task)
    return new_task

# Update an existing task
@app.put("/tasks/{task_id}", response_model=dict)
def update_task(task_id: int, updated_task: Task):
    task_index = next(
        (index for index, t in enumerate(tasks) if t["id"] == task_id), None
    )
    if task_index is None:
        raise HTTPException(status_code=404, detail="Task not found")

    tasks[task_index].update(
        {"title": updated_task.title, "description": updated_task.description, "status": updated_task.status}
    )
    return tasks[task_index]

# Delete a task
@app.delete("/tasks/{task_id}", response_model=dict)
def delete_task(task_id: int):
    task_index = next(
        (index for index, t in enumerate(tasks) if t["id"] == task_id), None
    )
    if task_index is None:
        raise HTTPException(status_code=404, detail="Task not found")

    deleted_task = tasks.pop(task_index)
    return deleted_task



def lambda_handler(event, context):
    return Mangum(app)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
