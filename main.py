# Status Codes & Response 
# Real world professional API
#  HTTP status code 
#  custom Response
#  Error handling basics

from fastapi import FastAPI, status, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

# Dependency Injections

# what is depends()
# Reusable logic
# Auth example intro

from fastapi import Depends, Header

def common_logic():
    return {
        "message": "common logic execute"
    }

@app.get("/")
def home(data = Depends(common_logic)):
    return data


# Auth inro
def verify_token(token: str = Header(None)):
    if token != "myToken":
        raise HTTPException(
            status_code = 401,
            detail= "Unauthorize"
        )
    return {
        "User":"Auth token "
    }


# here for testing we need to pass token in heade3r
@app.get("/get_token")
def get_token(user = Depends(verify_token)):
    return {
        "message":"Access granted",
        "user": user
    }


# ----------------------
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

# -----------------------

# Exception Handling
# HTTPException
# Custom exceptions
# global erro handler


# custom excepiton
@app.get("/items/{id}")
def get_items(id: int):
    if id != 1:
        raise HTTPException(
            status_code=404,
            detail= "Item not found"
        )
    return {
        "itemName": "Laptop",
        "price": 120000
    }
 

#  Custome error funciton 
class UserNotFoundException(Exception):
    def __init__(self, name:str):
        self.name = name

# global exception Handler
@app.exception_handler(UserNotFoundException)
def user_not_found(request:Request, exc:UserNotFoundException):
    return JSONResponse( 
        status_code = 404,
        content= {
            "status": "error",
            "message": f"user {exc.name} not found"
        }
    )

@app.get("/getItem/{name}")
def get_item_by_name(name:str):
    if name != "ram":
        raise UserNotFoundException(name)
    return {
        "name": name
    }
    