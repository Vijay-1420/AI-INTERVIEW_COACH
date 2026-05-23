from fastapi import FastAPI
from services.evaluator import evaluate_answer
from models.schema import AnswerRequest
from routes.interview import router

from database.db import engine
from database.models import Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include interview routes
app.include_router(router)

@app.get("/")
def home():
    return {"message": "AI Interview Coach Backend Running 🚀"}
