from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.base import Base
from app.database.database import engine

# Import models so SQLAlchemy registers them
from app.database import models

from app.api.routes.assistant import router as assistant_router
from app.api.routes.task import router as tasks_router

from app.middleware.exception_handler import register_exception_handlers
from app.middleware.logging import LoggingMiddleware


app = FastAPI(
    title="AI Task Assistant",
    version="1.0.0",
)

# Middleware
app.add_middleware(LoggingMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Change for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Exception Handlers
register_exception_handlers(app)

print(Base.metadata.tables.keys())

# Create database tables
Base.metadata.create_all(bind=engine)

# Routes
app.include_router(assistant_router)
app.include_router(tasks_router)


@app.get("/")
def health():
    return {
        "status": "running",
        "application": "AI Task Assistant",
    }