from pydantic import BaseModel 

class Register(BaseModel): 
    fullname: str
    username: str
    password: str 

class Login(BaseModel): 
    username: str 
    password: str 

