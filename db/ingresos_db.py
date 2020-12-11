from typing import Dict
from pydantic import BaseModel
from datetime import date

class ingreso(BaseModel):
    tipoIngreso: str
    origen: str
    valor: float
    descripcion: str
    fecha: date



database_users = Dict[str, ingreso]
database_users = {
    "juan23": ingreso(**{   "username":"juan30",
                            "password":"admin123",
                            "tipoIngreso":"salario",
                            "origen":"empleo",
                            "valor":1800000,
                            "descripcion":"salario que gana el trabajador",
                            "fecha":"2020-12-9"}),
    "maria25": ingreso(**{  "username":"maria25",
                            "password":"1234",
                            "tipoIngreso":"honorarios",
                            "origen":"horas extras",
                            "valor":350000,
                            "descripcion":"horas extras fines de semana",
                            "fecha":"2020-12-5"}),
}

def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None
        
def update_user(user_in_db: ingreso):
    database_users[user_in_db.username] = user_in_db
    return user_in_db   