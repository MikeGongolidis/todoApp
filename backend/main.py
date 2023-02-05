from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

DUMMY_TASK = {
    "1":
    {    "id": 1,
        "title": "skoupisma",
        "category-id": 1,
        "asignee-id": 1,
        "users-id": [1],
        "group-id": 1},
    "2":
    {    "id": 2,
        "title": "skoupisma",
        "category-id": 1,
        "asignee-id": 1,
        "users-id": [1, 2],
        "group-id": 1},
    "3":
    {    "id": 3,
        "title": "skoupisma",
        "category-id": 1,
        "users-id": [2],
        "asignee-id": 1,
        "group-id": 2},
}

DUMMY_CAT = {
    "id": 1,
    "title": "douleies spitiou",
    "color": "blue"
}

DUMMY_USER = {
    "id": 1,
    "name": "Mike",
    "group-id": 1
}

DUMMY_GROUP = {
    "id": 1,
    "name": "mike and electra",
    "users-id": [1, 2]
}

def find_tasks(val, dicts):
    tmp = []
    for v in dicts.values():
        if val in v['users-id']:
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
def list(user_id: int):
    
    return find_tasks(user_id, DUMMY_TASK)