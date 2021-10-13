from sqlalchemy import Column,Integer,String
from database import Base


class ProductD(Base):
    __tablename__ = 'product'
    
    id = Column(Integer,primary_key = True,index = True)
    Product = Column(String)
    Type = Column(String)
    Price = Column(Integer)
    Quantity = Column(Integer)
    Date_arrived = Column(String)
    Expiry_date = Column(String)
    Manufactured_date = Column(String)
    Where_bought = Column(String)
    
class Users(Base):
    __tablename__ = 'users'
    
    id = Column(Integer,primary_key = True,index = True)
    User_name = Column(String)
    Email = Column(String)
    Password = Column(String)