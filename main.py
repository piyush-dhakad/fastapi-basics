from fastapi import FastAPI

app = FastAPI()

#Home
@app.get("/")
def home():
    return { "name": "piyush" }

#About
@app.get("/about")
def about():
    return {"Name": "Hi i'm about "}


#users 
@app.get("/users")
def get_users():
    return { "data": [
        {"user": 1},
        {"user": 2},
        {"user": 3},
    ]}

#get User #path paramters
@app.get("/user/{user_id}")
def get_user(user_id:int):
    return {"user": user_id}


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