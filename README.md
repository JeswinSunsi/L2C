# Learn to Code - Python Web App

This project is a "Learn to Code" platform built with **Vue 3 (Vite)** and **FastAPI**. It features a complete authentication system, progress tracking, and interactive coding lessons.

## Project Structure

- `backend/`: FastAPI application with SQLite database and JWT authentication.
- `frontend/`: Vue 3 application with Pinia state management and Vue Router.

## Prerequisites

- Python 3.8+
- Node.js 16+

## Setup & Run

### Backend

1. Navigate to the backend folder:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
   python main.py
   ```
   The API will be available at `http://localhost:8000`.
   The database `sql_app.db` will be automatically created on the first run.

### Frontend

1. Navigate to the frontend folder:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the development server:
   ```bash
   npm run dev
   ```
   The app will be available at `http://localhost:5173`.

## Features

- **Authentication**: User registration and login (JWT-based).
- **Course Plan**: Dashboard showing all lessons and completion status.
- **Progress Tracking**: Tracks completed lessons and scores.
- **Interactive Lessons**: Quizzes, Logic Builders, and Visual Debuggers.
- **Production Ready**: Structured for scalability with separate routers, models, and state management.

## Tech Stack

- **Backend**: FastAPI, SQLAlchemy, SQLite, Passlib, Python-Jose
- **Frontend**: Vue 3, Vite, Pinia, Vue Router, Tailwind CSS


- **Interactive Lessons**: Quizzes, Logic Builders, Visual Debuggers, Method Labs, and Slicing Playgrounds.
- **Gamified Progression**: Unlock lessons as you complete them.
- **Modern UI**: Built with Tailwind CSS for a clean, responsive design.
