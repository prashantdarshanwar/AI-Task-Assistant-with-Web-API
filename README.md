# 🤖 AI Task Assistant

An AI-powered Task Management Assistant that converts **natural language task requests** into structured tasks using a Large Language Model (Groq), stores them in SQLite, and displays them through a simple web interface.



---

# 📌 Problem Statement

Build a full-stack AI Task Assistant that:

- Accepts natural language requests such as:

> Create a task to fix login bug next Friday high priority

- Uses an LLM to extract:

  - Task Title
  - Due Date
  - Priority

- Stores the task in SQLite
- Displays tasks on a minimal frontend
- Provides a FastAPI REST API

---

# 🚀 Features

✅ Natural Language Task Creation

✅ AI-powered Task Parsing (Groq LLM)

✅ Automatic Date Extraction

✅ Natural Language Date Parsing

✅ SQLite Database

✅ FastAPI REST API

✅ Swagger Documentation

✅ Responsive Frontend

✅ Task Priority Detection

✅ Input Validation (Pydantic)

✅ Error Handling

✅ Logging Middleware

✅ Modular Architecture

---

# 🛠 Tech Stack

## Backend

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic v2
- Groq API
- dateparser
- python-dotenv

## Frontend

- HTML5
- CSS3
- Vanilla JavaScript

---

# 📂 Project Structure

```
AI-TASK-ASSISTANT
│
├── backend
│   │
│   ├── app
│   │   ├── api
│   │   ├── core
│   │   ├── crud
│   │   ├── database
│   │   ├── llm
│   │   ├── middleware
│   │   ├── schemas
│   │   ├── services
│   │   ├── utils
│   │   ├── tests
│   │   └── main.py
│   │
│   ├── logs
│   ├── requirements.txt
│   ├── .env.example
│   └── tasks.db
│
├── frontend
│   ├── assets
│   ├── css
│   ├── js
│   ├── screenshots
│   └── index.html
│
├── docker
│
├── docs
│
├── README.md
├── LICENSE
└── .gitignore
```

---

# ⚙️ Prerequisites

Before running the project install:

- Python 3.11+
- Git
- Groq API Key

---

# 🔑 Get Groq API Key

1. Visit

https://console.groq.com

2. Login

3. Generate an API Key

4. Copy the API Key

---

# ⚙️ Clone Repository

```bash
git clone https://github.com/prashantdarshanwar/AI-Task-Assistant-with-Web-API.git

cd AI-Task-Assistant-with-Web-API
```

---

# ⚙️ Backend Setup

Move into backend

```bash
cd backend
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configure Environment Variables

Create a file named

```
.env
```

inside

```
backend/
```

Add

```env
GROQ_API_KEY=your_groq_api_key

MODEL=llama-3.3-70b-versatile

DATABASE_URL=sqlite:///tasks.db
```

Example

```env
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxx

MODEL=llama-3.3-70b-versatile

DATABASE_URL=sqlite:///tasks.db
```

---

# ▶️ Start Backend

Inside backend

```bash
uvicorn app.main:app --reload
```

Server

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

# 🌐 Frontend Setup

Open another terminal.

Move into frontend

```bash
cd frontend
```

Run

```bash
python -m http.server 5500
```

Open

```
http://127.0.0.1:5500
```

---

# 🧪 Testing the Application

Open the frontend.

Type

```
Create task to fix login bug next Friday high priority
```

Click

```
Create Task
```

You should see

```
Title:
Fix login bug

Priority:
HIGH

Due Date:
2026-07-24
```

---

# 📡 API Endpoints

## Create Task

POST

```
/assistant
```

Request

```json
{
    "query":"Create task to fix login bug next Friday high priority"
}
```

Response

```json
{
    "id":1,
    "title":"Fix login bug",
    "due_date":"2026-07-24",
    "priority":"high",
    "created_at":"2026-07-18T13:15:21"
}
```

---

## Get All Tasks

GET

```
/tasks
```

Response

```json
[
  {
    "id":1,
    "title":"Fix login bug",
    "due_date":"2026-07-24",
    "priority":"high"
  }
]
```

---

# 📅 Supported Natural Language Dates

Examples

```
today

tomorrow

Friday

next Friday

next Monday

next week

next month

next month Saturday

next month Friday

after 2 weeks

in 3 days

25 July

July 25

25/07/2026

2026-07-25
```

---

# 🏗 Architecture

```
                  User

                    │

                    ▼

       HTML + CSS + JavaScript

                    │

                    ▼

             FastAPI Backend

                    │

                    ▼

             Groq LLM Service

                    │

                    ▼

          JSON Validation Layer

                    │

                    ▼

      Natural Language Date Parser

                    │

                    ▼

            SQLAlchemy ORM

                    │

                    ▼

              SQLite Database

                    │

                    ▼

             JSON Response

                    │

                    ▼

                Frontend
```

---

# 🔄 Workflow

```
User enters task

↓

Frontend

↓

POST /assistant

↓

Groq LLM

↓

Structured JSON

↓

Validation

↓

Date Parser

↓

SQLite

↓

Response

↓

Task displayed on UI
```

---

# 📷 Screenshots

## Home

```
frontend/screenshots/home.png
```

---

## Task Created

```
frontend/screenshots/task-created.png
```

---

## Swagger

```
frontend/screenshots/swagger.png
```

---

# 🐳 Docker (Optional)

Build

```bash
docker compose up --build
```

Backend

```
http://localhost:8000
```

---

# 🧪 Future Improvements

- JWT Authentication
- User Login
- PostgreSQL
- Docker Deployment
- Unit Tests
- Task Editing
- Task Search
- Task Filtering
- Dark Theme
- Notifications
- Calendar Integration

---

# 📝 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Prashant Darshanwar**

Email

```
prashantdarshanwar70715@gmail.com
```

GitHub

```
https://github.com/prashantdarshanwar/AI-Task-Assistant-with-Web-API.git
```

---

# 🙏 Acknowledgements

- Pyngyn
- FastAPI
- Groq
- SQLAlchemy
- Pydantic
- dateparser

---

# ✅ Submission Checklist

- [x] FastAPI Backend
- [x] AI-powered Task Parsing
- [x] SQLite Database
- [x] Natural Language Date Parsing
- [x] REST API
- [x] Frontend
- [x] Swagger Documentation
- [x] README
- [x] Environment Setup
- [x] Installation Guide
- [x] API Key Instructions
- [x] Local Run Instructions