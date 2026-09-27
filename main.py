from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

# Address Model
class Address(BaseModel):
    city:str
    pincode:int = 0

# user Model
class User(BaseModel):
    name:str
    age:int
    address:Address

# Request body
@app.post("/create-user")
def create_user(user:User):
    data = user.model_dump()
    return { "message": "User Created",
    "data" : data
    }
 


# pydantic Base Model
# create schemas
# data validation
# nested models  



#Home
@app.get("/")
def home():
    return { "name": "piyush" }

# Query params
@app.get("/user")
def get_user_by_id(param:str = None):
    return { "data":param}


#query params default parameters
@app.get("/products")
def get_products(limit:int = 10):
    return { "limit": limit}

# multpile query params
@app.get("/items")
def get_items(name:str = None, price:int = 0):
    return {
        "name": name ,
        "price": price
    }