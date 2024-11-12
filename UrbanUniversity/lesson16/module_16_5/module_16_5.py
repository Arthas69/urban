from typing import Annotated, List

from fastapi import FastAPI, status, Path, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

templates = Jinja2Templates(directory='templates')

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/')
async def main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request=request, name='users.html', context={'users': users})


@app.get('/user/{user_id}')
async def get_user_info(request: Request, user_id: int) -> HTMLResponse:
    try:
        user = users[user_id - 1]
        return templates.TemplateResponse(request=request, name='users.html', context={'user': user})
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.post('/user/{username}/{age}')
async def add_info(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example='24')]) -> User:
    if users:
        idx = max(users, key=lambda x: x.id).id + 1
    else:
        idx = 1
    new_user = User(id=idx, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/users/{user_id}/{username}/{age}')
async def update_user(
        user_id: int,
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example='24')]) -> User:
    try:
        user = users[user_id - 1]
        user.username = username
        user.age = age
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/users/{user_id}')
async def delete_user(user_id: int) -> User:
    try:
        user_del = users.pop(user_id - 1)
        return user_del
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
