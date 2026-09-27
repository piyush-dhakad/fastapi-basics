from fastapi import FastAPI

app = FastAPI()

# Request body
@app.post("/create-user")
def create_user(user:dict):
    return { "message": "User Created",
    "data" : {
        "name":user.get("name"),
        "age":user.get("age")
    }}
 












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