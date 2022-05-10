from fastapi import FastAPI, Body, Depends
from app.auth.auth_beare import JWTBearer
from model import PostSchema, UserSchema, UserLoginSchema
from app.auth.auth_handler import signJWT
from app.auth.auth_handler import signJWT


posts = [
    {
        "id": 1,
        "title": "Pancake",
        "content": "Lorem"
    }
] 

users = []

app = FastAPI()

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False

@app.post("/user/login", tags=["user"])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return{
        "error": "Falha no login!"
    }

@app.post("/user/signup", tags=["user"])
async def create_user(user: UserSchema = Body(...)):
    users.append(user)
    return signJWT(user.email)

@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Bem vindo ao meu site."}


@app.get("/posts", tags=["posts"])
async def get_posts() -> dict:
    return {"data": posts}


@app.get("/posts/{id}", tags=["posts"])
async def get_single_post(id: int) -> dict:
    if id > len(posts):
        return{
            "error": "Cadê o ID mano"
        }
    
    for post in posts:
        if post["id"] == id:
            return{
                "data": post
            }    
            

@app.post("/posts", dependencies=[Depends(JWTBearer())], tags=["posts"])
async def add_post(post: PostSchema) -> dict:
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "data": "post added"
    }
