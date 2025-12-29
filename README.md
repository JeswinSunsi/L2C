# Learn to Code - Python Web App

This project is a "Learn to Code" platform built with **Vue 3 (Vite)** and **FastAPI**.

## Project Structure

- `backend/`: FastAPI application serving lesson content.
- `frontend/`: Vue 3 application for the user interface.

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

- **Interactive Lessons**: Quizzes, Logic Builders, Visual Debuggers, Method Labs, and Slicing Playgrounds.
- **Gamified Progression**: Unlock lessons as you complete them.
- **Modern UI**: Built with Tailwind CSS for a clean, responsive design.
