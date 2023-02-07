from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

DUMMY_TASK = {
    1:
    {    "id": 1,
        "title": "skoupisma",
        "category_id": 1,
        "asignee_id": 1,
        "users_id": [1],
        "group_id": 1},
    2:
    {    "id": 2,
        "title": "skoupisma",
        "category_id": 1,
        "asignee_id": 1,
        "users_id": [1, 2],
        "group_id": 1},
    3:
    {    "id": 3,
        "title": "skoupisma",
        "category_id": 1,
        "users_id": [2],
        "asignee_id": 1,
        "group_id": 2},
}

DUMMY_CAT = {
    "id": 1,
    "title": "douleies spitiou",
    "color": "blue"
}

DUMMY_USER = {
    "id": 1,
    "name": "Mike",
    "group_id": 1
}

DUMMY_GROUP = {
    "id": 1,
    "name": "mike and electra",
    "users_id": [1, 2]
}

class Task(BaseModel):
    id: int
    title: str
    category_id: int
    asignee_id: int
    users_id: list
    group_id: int

def find_tasks(user_id, tasks):
    tmp = []
    for v in tasks.values():
        if user_id in v['users_id']:
            tmp.append(v)

    if len(tmp) > 0:
        return tmp
    return "Tasks not found"

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{user_id}")
def list_tasks(user_id: int):
    
    return find_tasks(user_id, DUMMY_TASK)

@app.post("/items/{user_id}")
def insert(user_id: int, task: Task):
    new_task_key = len(DUMMY_TASK) + 1
    DUMMY_TASK[new_task_key] = task.dict()
    
    return DUMMY_TASK

@app.delete("/items/{user_id}")
def delete(user_id: int, task_id: int):
    DUMMY_TASK.pop(task_id)
    return DUMMY_TASK