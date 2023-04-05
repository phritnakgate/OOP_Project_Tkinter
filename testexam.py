from fastapi import FastAPI

app = FastAPI()

from datetime import datetime
from courses import *
from user import *
from enroll import *
from exam import *
from dto import *

course_system = CourseSystem()

teacher1 = Teacher("teach1", 
                  "123456", 
                  "teacher1@gmail.com", 
                  "tea", "cher", "Male", datetime(2003, 12, 4), "D.Eng",
                  "Bangkok", "Thailand", "KMITL")

student1 = Student("ffwatcharin", 
                  "firstbigdick", 
                  "ffwatcharin@gmail.com", "Watcharin", "Humthong", "Male",
                  datetime(2004, 1, 16), "Undergraduated","Nonthaburi", "Thailand")

course1 = Courses("SOFT001", 
                 "Object Oriented Programming", 
                 "Learn writing oop", teacher1.get_username, "Software", "All Ages",
                 "To understanding OOP", "10", "10", datetime.now(), "teacher1@gmail.com")


oop_exam = CourseExam(course1.get_title)

@app.post("/exam/question and answer")
async def add_question(data : Problems):
    q_list = []
    for q , a in data.questions:
        q_list.append(ExamItem(q, a))
    oop_exam.add_question_ans(q_list)
    return {"message": "Question and Answer added successfully"}

@app.get("/exam")
async def get_exam():
    return oop_exam._exam_list

@app.post("/exam")
async def take_exam(student_answers: list):
    score = oop_exam.do_exam(student_answers)
    return {"score": score}   








