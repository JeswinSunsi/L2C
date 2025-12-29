from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load content
def load_content():
    with open("content.json", "r") as f:
        return json.load(f)

@app.get("/lessons")
def get_lessons():
    content = load_content()
    # Return summary list
    return [{"id": lesson["id"], "title": lesson["title"], "type": lesson["type"]} for lesson in content]

@app.get("/lessons/{lesson_id}")
def get_lesson(lesson_id: int):
    content = load_content()
    lesson = next((l for l in content if l["id"] == lesson_id), None)
    if lesson:
        return lesson
    raise HTTPException(status_code=404, detail="Lesson not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
