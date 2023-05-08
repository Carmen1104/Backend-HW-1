from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class todoList(BaseModel):
    title: str
    desc: str
    status: str

class UpdatetodoList(BaseModel):
    title: Optional [str] = None
    desc: Optional [str] = None
    status: Optional [str] = None

todo_list = {
    1: todoList(title= "do homework", desc= "deadline tmr", status= "done"),
    2: todoList(title= "make food", desc= "today make chicken steak", status= "not done"),
    3: todoList(title= "do laundry", desc= "clothes are piling", status= "not done"),
    4: todoList(title= "pick up siblings", desc= "they go home at 3 today", status= "not done"),
    5: todoList(title= "feed sugar gliders", desc= "feed the babies too", status= "not done")
}

#GET
#Path Parameter
@app.get("/")
def index():
    return {"Hello" : "Hello, This is a backend for a todo list app."}

@app.get("/get-task/{todo_id}")
def get_task(todo_id: int = Path(description="Enter id of task")):
    return todo_list[todo_id]

#get task by title
@app.get("/get-task-by-title/{title}")
def get_task(title: str):
    for todo_id in todo_list:
        if todo_list[todo_id].title == title:
            return todo_list[todo_id]
    return ("Task don't exist")

#POST
@app.post("/create-todo/{todo_id}")
def add_task(todo_id:int, todo:todoList):
    if todo_id in todo_list:
        return("error: Task Id already exist")
    todo_list[todo_id] = todo
    return todo_list[todo_id]

#UPDATE
@app.put("/update-task/{todo_id}")
def update_task(todo_id: int, task: UpdatetodoList):
    if  todo_id not in todo_list:
            return("error: Task Id doesn't Exist")
    
    if task.title != None:
        todo_list[todo_id].title = task.title

    if task.desc != None:
        todo_list[todo_id].desc = task.desc

    if task.status != None:
        todo_list[todo_id].status = task.status

    return todo_list[todo_id]

#DELETE
@app.delete("/delete-task/{todo_id}")
def delete_task(todo_id: int):
    if todo_id not in todo_list:
        return("error: Task Id doesn't Exist")
    del todo_list[todo_id]
    return {"data": "delete successful"}
