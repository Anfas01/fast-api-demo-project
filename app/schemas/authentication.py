from pydantic import BaseModel

class UserRegister(BaseModel):
    username: str
    email: str
    password: str
    

class UserRegisterResponse(BaseModel):
    username: str
    
    
    class Config:
        from_attributes = True