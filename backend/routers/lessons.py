from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import json
import database, models, schemas, security

router = APIRouter(
    prefix="/lessons",
    tags=["lessons"]
)

# Load content once
with open("content.json", "r") as f:
    CONTENT = json.load(f)

@router.get("/", response_model=List[schemas.Lesson])
def get_lessons():
    return [{"id": l["id"], "title": l["title"], "type": l["type"], "description": l.get("description")} for l in CONTENT]

@router.get("/{lesson_id}")
def get_lesson(lesson_id: int):
    lesson = next((l for l in CONTENT if l["id"] == lesson_id), None)
    if lesson:
        return lesson
    raise HTTPException(status_code=404, detail="Lesson not found")

@router.post("/{lesson_id}/complete", response_model=schemas.LessonProgress)
def complete_lesson(
    lesson_id: int, 
    progress: schemas.LessonProgressCreate, 
    current_user: models.User = Depends(security.get_current_user),
    db: Session = Depends(database.get_db)
):
    # Check if lesson exists
    lesson = next((l for l in CONTENT if l["id"] == lesson_id), None)
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")

    # Check if progress already exists
    db_progress = db.query(models.LessonProgress).filter(
        models.LessonProgress.user_id == current_user.id,
        models.LessonProgress.lesson_id == lesson_id
    ).first()

    if db_progress:
        db_progress.completed = progress.completed
        db_progress.score = progress.score
    else:
        db_progress = models.LessonProgress(
            user_id=current_user.id,
            lesson_id=lesson_id,
            completed=progress.completed,
            score=progress.score
        )
        db.add(db_progress)
    
    db.commit()
    db.refresh(db_progress)
    return db_progress
