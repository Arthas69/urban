from typing import Annotated, List

from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel


app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
async def main_page() -> List[User]:
    return users


@app.post('/users/{username}/{age}')
async def add_info(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example='24')]) -> User:
    idx = len(users) + 1
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
