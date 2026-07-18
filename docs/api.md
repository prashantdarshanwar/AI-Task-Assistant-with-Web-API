# 📘 AI Task Assistant API Documentation

## Base URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# Authentication

No authentication is required.

---

# Content Type

All requests should use:

```
Content-Type: application/json
```

---

# Endpoints

---

# 1. Health Check

Returns the application status.

### Endpoint

```
GET /
```

### Request

```http
GET /
```

### Response

```json
{
    "status": "running",
    "application": "AI Task Assistant"
}
```

---

# 2. Create Task Using Natural Language

Converts a natural language request into a structured task using Groq LLM.

### Endpoint

```
POST /assistant
```

---

## Request Body

```json
{
    "query": "Create a task to fix login bug next Friday high priority"
}
```

---

## Successful Response

```json
{
    "id": 1,
    "title": "Fix login bug",
    "due_date": "2026-07-24",
    "priority": "high",
    "created_at": "2026-07-18T13:20:10"
}
```

---

## Error Response

```json
{
    "success": false,
    "message": "Unable to parse due date."
}
```

---

# Supported Natural Language Examples

The assistant understands:

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

after 1 month

in 3 days

in 5 weeks

25 July

July 25

25/07/2026

2026-07-25
```

---

# Priority Detection

Accepted values

```
low

medium

high
```

If no priority is provided:

```
medium
```

is used automatically.

---

# 3. Get All Tasks

Returns all stored tasks.

### Endpoint

```
GET /tasks
```

---

## Request

```http
GET /tasks
```

---

## Response

```json
[
    {
        "id": 1,
        "title": "Fix login bug",
        "due_date": "2026-07-24",
        "priority": "high",
        "created_at": "2026-07-18T13:20:10"
    },
    {
        "id": 2,
        "title": "Deploy backend",
        "due_date": "2026-07-29",
        "priority": "medium",
        "created_at": "2026-07-18T13:22:15"
    }
]
```

---

# 4. Delete Task (Optional)

> Available only if implemented.

### Endpoint

```
DELETE /tasks/{id}
```

---

## Example

```
DELETE /tasks/1
```

---

## Response

```json
{
    "message": "Task deleted successfully."
}
```

---

# HTTP Status Codes

| Status Code | Description |
|-------------|-------------|
| 200 | Success |
| 201 | Task Created |
| 400 | Bad Request |
| 404 | Task Not Found |
| 422 | Validation Error |
| 500 | Internal Server Error |

---

# Request Flow

```
Client

↓

POST /assistant

↓

FastAPI

↓

Groq LLM

↓

Extract JSON

↓

Validation

↓

Date Parser

↓

SQLite

↓

JSON Response

↓

Frontend
```

---

# Example Requests

## Example 1

Request

```json
{
    "query": "Create task to deploy backend tomorrow high priority"
}
```

Response

```json
{
    "title": "Deploy backend",
    "due_date": "2026-07-19",
    "priority": "high"
}
```

---

## Example 2

Request

```json
{
    "query": "Create task to update API documentation next month Saturday"
}
```

Response

```json
{
    "title": "Update API documentation",
    "due_date": "2026-08-01",
    "priority": "medium"
}
```

---

## Example 3

Request

```json
{
    "query": "Create task to backup database after 2 weeks"
}
```

Response

```json
{
    "title": "Backup database",
    "due_date": "2026-08-01",
    "priority": "medium"
}
```

---

# Error Handling

The API validates:

- Empty task title
- Invalid priority values
- Invalid JSON
- Unsupported dates
- Missing request body
- Database errors

Example:

```json
{
    "success": false,
    "message": "Task title is required."
}
```

---

# Technologies Used

- FastAPI
- Groq LLM
- SQLAlchemy
- SQLite
- Pydantic
- dateparser
- Python 3.11

---

# Testing with Swagger

Start the backend:

```bash
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

Use the interactive Swagger UI to test all endpoints.

---

# Version

Current Version

```
1.0.0
```

---

# Maintainer

**Prashant Darshanwar**

Email

```
prashantdarshanwar70715@gmail.com
```