from fastapi import APIRouter
from backend.services.evaluator import evaluate_answer
from backend.models.schema import AnswerRequest

from database.db import SessionLocal
from database.models import InterviewResponse

import random

router = APIRouter()

questions = {
    1: {"question": "Tell me about yourself", "difficulty": "Easy"},
    2: {"question": "What are your strengths?", "difficulty": "Easy"},
    3: {"question": "Explain OOP concepts", "difficulty": "Medium"},
    4: {"question": "What is recursion?", "difficulty": "Medium"}
}

current_question_id = None

# ---------------- GET QUESTION ----------------

@router.get("/question")
def get_question():

    global current_question_id

    q_id = random.choice(list(questions.keys()))

    current_question_id = q_id

    return {
        "question": questions[q_id]["question"],
        "difficulty": questions[q_id]["difficulty"]
    }

# ---------------- SUBMIT ANSWER ----------------

@router.post("/answer")
def submit_answer(data: AnswerRequest):

    global current_question_id

    if current_question_id is None:
        return {
            "error": "No active question found"
        }

    score, feedback = evaluate_answer(data.answer)

    result = {
        "question": questions[current_question_id]["question"],
        "answer": data.answer,
        "score": score,
        "feedback": feedback
    }

    # DATABASE SAVE
    db = SessionLocal()

    response_entry = InterviewResponse(
        question=result["question"],
        answer=result["answer"],
        score=result["score"],
        feedback=result["feedback"]
    )

    db.add(response_entry)

    db.commit()

    db.close()

    return result