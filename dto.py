from typing import List
from pydantic import BaseModel


# Define the question model
class Problem(BaseModel):
    question: str
    answer: str

# Define the questions model
class Problems(BaseModel):
    questions: List[Problem] 
    
class EditExam(BaseModel) :
    question: str
    answer: str
