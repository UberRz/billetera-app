from pydantic import BaseModel
from _datetime import date

class UserIn(ingreso):
    username: str
    password: str
    
class UserOut(ingreso):
    username: str
    ingreso: str
    origen:str
    valor:float
    descripcion:str
    fecha: date