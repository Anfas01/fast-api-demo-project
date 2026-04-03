from pydantic import BaseModel

class UserRegister(BaseModel):
    username: str
    email: str
    password: str
    

class UserRegisterResponse(BaseModel):
    username: str
    
    
    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    username: str
    password: str


class UserLoginResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str