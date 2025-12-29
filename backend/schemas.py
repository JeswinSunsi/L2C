from pydantic import BaseModel
from typing import List, Optional

class LessonProgressBase(BaseModel):
    lesson_id: int
    completed: bool
    score: int

class LessonProgressCreate(LessonProgressBase):
    pass

class LessonProgress(LessonProgressBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    progress: List[LessonProgress] = []

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class Lesson(BaseModel):
    id: int
    title: str
    type: str
    description: Optional[str] = None
    # Add other fields as needed from content.json
