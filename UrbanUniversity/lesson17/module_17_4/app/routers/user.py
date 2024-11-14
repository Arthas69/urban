from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select, insert, update, delete
from slugify import slugify

from app.backend.db_depends import get_db
from app.models import User, Task
from app.schemas import CreateUser, UpdateUser

router = APIRouter(prefix='/user', tags=['user'])


@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    print(users)
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No users found')
    return users


@router.get('/user_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(user_id == User.id))
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')
    return user


@router.post('/create')
async def create_user(
        db: Annotated[Session, Depends(get_db)],
        user_data: CreateUser):
    user = db.scalar(select(User).where(user_data.username == User.username))
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='User with this username already exists')

    db.execute(insert(User).values(
        username=user_data.username,
        firstname=user_data.firstname,
        lastname=user_data.lastname,
        age=user_data.age,
        slug=slugify(user_data.username)
    ))

    db.commit()

    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction_id': 'Successful'
    }


@router.put('/update')
async def update_user(
        db: Annotated[Session, Depends(get_db)],
        user_id: int,
        user_data: UpdateUser
):
    user = db.scalar(select(User).where(user_id == User.id))
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')
    db.execute(update(User).where(user_id == User.id).values(
        firstname=user_data.firstname,
        lastname=user_data.lastname,
        age=user_data.age,
    ))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'User was updated successfully'
    }


@router.delete('/delete')
async def delete_user(
        db: Annotated[Session, Depends(get_db)],
        user_id: int
):
    user = db.scalar(select(User).where(user_id == User.id))
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")

    db.execute(delete(User).where(user_id == User.id))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'User was deleted successfully'
    }
