from pydantic import BaseModel

class Productin(BaseModel):
    Product:str
    Type:str
    Price:int
    Quantity:int
    Date_arrived:str
    Manufactured_date:str
    Expiry_date:str
    Where_bought:str
    
class UserM(BaseModel):
    User_name:str
    Email:str
    
    