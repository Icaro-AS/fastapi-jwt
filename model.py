from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):
    id: int = Field(default = None)
    title: str = Field(...)
    content: str = Field(...)
    
    class Config:
        schema_extra ={
            "example" : {
                "title": "Securing FastAPI applications with JWT",
                "content": "Criando aplicações seguras."
                
            }
        } 

class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    
    class Config:
        schema_extra ={
            "example":{
                "fullname": "Alana Loren",
                "email": "alana@gmail.com",
                "password": "weakpassword"
            }
        }
            
class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)
    
    class Config:
        schema_extra = {
            "example":{
                "email": "alana@gmail.com",
                "password": "weakpassword"
            }
        }