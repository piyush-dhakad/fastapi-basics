# Status Codes & Response 
# Real world professional API
#  HTTP status code 
#  custom Response
#  Error handling basics

from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

#  200 = success 
#  201 = create data
#  400 = bad request 
#  404 = not found
#  500 = server error


@app.post("/create_user", status_code= status.HTTP_201_CREATED)
def create_user():
    return {
        "message": "User Created"
    }

@app.get("/user")
def get_user():
    return {
        "status": "Success",
        "message": "user fetch",
        "data": {
            "name": "varun",
            "age": 28
        }
    }

# Error Handling baseics

@app.get("/users/{id}")
def get_users(id:int):
    if id != 1:
        # raise BaseException()
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return {
        "user" : "varun"
    }