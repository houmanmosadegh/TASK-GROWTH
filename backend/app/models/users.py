from sqlalchemy import Column,Integer,String
from app.database import Base 

class User(Base): 
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True)
    fullname = Column(String(50),index=True,nullable=False)  
    username = Column(String(100),unique=True,nullable=False) 
    password = Column(String(250),nullable=False) 
    
    
