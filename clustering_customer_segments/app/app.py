from typing import Dict, List

import models
from config import settings
from database import SessionLocal, engine
from fastapi import BackgroundTasks, Depends, FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from pydantic.main import BaseModel
from sqlalchemy.orm import Session

# Create db & table with SQLalchemy
models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Pydantic classes
class ImageRequest(BaseModel):
    image: str


# FastAPI
app = FastAPI(
    title=settings.name, description=settings.description, version=settings.version
)

# Jinja2Templates
templates = Jinja2Templates(
    directory="D:/CompSci/Projects/digit-drawing-prediction/digit_recognition/templates/"
)

# Routes
@app.get("/")
async def root():
    return {"message": "Hello World"}
