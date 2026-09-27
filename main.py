from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todo = [   {
      "id": 2,
      "title": "this is second totod",
      "copleted": True
    },
    {
      "id": 3,
      "title": "this is first todo",
      "copleted": False
    }]

class Todo(BaseModel):
    id:int
    title:str
    copleted:bool = False

# Create todo
@app.post("/create_todo")
def create_todo(todos: Todo):
    data = todos.model_dump()

    if len(todo) == 0:
        todo.append(data)
        return {"message": "todo added successfully", "data": data}

    for item in todo:
        if item.get("id") == data.get("id"):
            return {"message": "todo already exist", "data": data}

    # loop finished, no match found → safe to append
    todo.append(data)
    return {"message": "todo added successfully", "data": data}

@app.get("/todos")
def get_totods():
    return {
            "message": "todo fetch scueesfully",
            "data":todo
        }


@app.put("/update_todo/{id}")
def update_todo(todos: Todo, id: int):
    data = todos.model_dump()

    for index, item in enumerate(todo):          # iterate your global list
         if item.get("id") == id:                      # compare dicts
            todo[index] = data
            return {
                "message": "todo updated successfully",
                "data": data,
            }

    return {
        "message": "todo not found",
        "data": None,
    }

# CRUD opertions
# create api 
# read api
# update api 
# delete api 

# Example project Todo API