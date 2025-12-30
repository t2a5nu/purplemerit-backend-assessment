# PurpleMerit Backend Assessment

## Tech Stack
- Python
- Flask
- SQLite
- SQLAlchemy
- JWT Authentication

## Features
- User Registration
- User Login
- JWT-based Authentication
- Role-based Access Control

## Setup Instructions

1. Create virtual environment
   python -m venv venv

2. Activate environment
   venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Run server
   python app.py

## API Endpoints

POST /register  
POST /login  
GET /profile (Protected)

## Sample Credentials
username: admin  
password: admin123  
role: admin
## Live Deployment

The backend API is deployed on Vercel.

Due to Vercel’s serverless execution model and SQLite filesystem limitations,
the Flask application throws a runtime error in production.

All API endpoints were tested and verified successfully in the local environment.
## Notes
- A `.gitignore` file is included in the GitHub repository.
- Due to ZIP export limitations on Windows/mobile, `.gitignore` may not appear in the attached ZIP.