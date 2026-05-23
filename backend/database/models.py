from sqlalchemy import Column, Integer, String
from database.db import Base

class InterviewResponse(Base):

    __tablename__ = "responses"

    id = Column(Integer, primary_key=True, index=True)

    question = Column(String)

    answer = Column(String)

    score = Column(Integer)

    feedback = Column(String)