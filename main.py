## Response Model ##
# Response validation
# Hide sensitive data
# output formatting


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    password: str

class UserResponse(BaseModel):
    name: str
    age: int

# response_model=UserResponse
@app.get("/user", response_model=UserResponse)
def get_user():

    return { 
        "name": "Piyush Dhakad",
        "age": "26",
        "password": "1234"
    }