from typing import Annotated

from fastapi import FastAPI, Path


app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def main_page():
    return users


@app.post('/users/{username}/{age}')
async def add_info(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example='24')]):
    idx = str(int(max(users, key=int)) + 1)
    users[idx] = f'Имя: {username}, Возраст: {age}'
    return {'message': f'User {idx} is registered'}


@app.put('/users/{user_id}/{username}/{age}')
async def update_user(
        user_id: str,
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example='24')]):
    if user_id in users:
        users[user_id] = f'Имя: {username}, Возраст: {age}'
        return {'message': f'User {user_id} is updated'}


@app.delete('/users/{user_id}')
async def delete_user(user_id: str):
    if user_id in users:
        del users[user_id]
        return {'message': f'User {user_id} is deleted'}
