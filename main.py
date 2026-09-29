#  path query body params
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    age:int

usersList = []

@app.get("/create_user")
def create_user(user:User):
    usersList.append(user.model_dump())
    return {
        "message": "User created",
        "data": user
    }

@app.put("/users/{user_id}")
def update_user(user_id:int, user:User, notify:bool = False):
    if user_id < len(usersList):
        usersList[user_id] = user.model_dump()

        return {
            "message": "User Updated",
            "notify": notify,
            "data": user
        }
    return {
        "error": "someting went wrong"
    }