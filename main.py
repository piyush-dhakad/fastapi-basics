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

#get User
@app.get("/user/{user_id}")
def get_user(user_id):
    return {"user": user_id}