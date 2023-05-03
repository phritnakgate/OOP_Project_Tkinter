from typing import List
from pydantic import BaseModel


# Define the question model
class AddQuesDTO(BaseModel):
    question: str
    answer: str

# Define the questions model
class QuestListDTO(BaseModel):
    questions: List[AddQuesDTO] 
    
class EditExamDTO(BaseModel) :
    question: str
    answer: str    

class AddReviewDTO(BaseModel):
    user : str
    score : int
    comment : str
    refcode : str