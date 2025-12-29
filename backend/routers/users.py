from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
import database, models, schemas, security

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/me", response_model=schemas.User)
async def read_users_me(current_user: models.User = Depends(security.get_current_user)):
    return current_user

@router.get("/me/progress", response_model=List[schemas.LessonProgress])
async def read_user_progress(current_user: models.User = Depends(security.get_current_user), db: Session = Depends(database.get_db)):
    return current_user.progress
