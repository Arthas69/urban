from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete, insert
from slugify import slugify

from app.backend.db_depends import get_db
from app.models import User, Task
from app.schemas import CreateTask, UpdateTask


router = APIRouter(prefix='/task', tags=['task'])


@router.get('/all_tasks')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    if not tasks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No tasks found')
    return tasks


@router.get('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task was not found')
    return task


@router.post('/create')
async def create_task(
        db: Annotated[Session, Depends(get_db)],
        task_data: CreateTask,
        user_id: int
):
    task = db.scalar(select(Task).where(Task.slug == (task_slug := slugify(task_data.title))))
    if task:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'Task with this title already exists')
    user = db.scalar(select(User).where(User.id == user_id))
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')
    db.execute(insert(Task).values(
        title=task_data.title,
        content=task_data.content,
        priority=task_data.priority,
        slug=task_slug,
        user_id=user_id)
    )
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }


@router.put('/update')
async def update_task(
        db: Annotated[Session, Depends(get_db)],
        task_id: int,
        task_data: UpdateTask
):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task was not found')
    db.execute(update(Task).where(Task.id == task_id).values(
        title=task_data.title,
        content=task_data.content,
        priority=task_data.priority)
    )
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Task was updated successfully'
    }


@router.delete('/delete')
async def delete_task(
        db: Annotated[Session, Depends(get_db)],
        task_id: int
):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task was not found")
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Task was deleted successfully'
    }

