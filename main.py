from fastapi import FastAPI
from db.ingresos_db import database_users
from fastapi import HTTPException
from db.ingresos_db import ingreso

app=FastAPI()

@app.get("/")
async def root():
    return {"message":"Bienvenido a su Billetera Virtual"}

@app.get("/users")
async def users():
    return {"message":database_users}

@app.get("/users/{username}")
async def get_user_ingreso(username:str):
    if username in database_users:
         return{"message":database_users[username]}
    raise HTTPException(status_code=404,detail="Usuario no se encuetnra en db")


@app.post("/users/")
async def create_user(user: ingreso):
    database_users[user.username]=user
    return user

@app.put("/crear/")
async def create_user(user :ingreso):
    database_users[user.username] = user 
    return user
