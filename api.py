from fastapi import FastAPI
from user import *
from system import *
from datetime import datetime
from courses import *
from exam import *
from dto import *

# --- Creation Test --- #
teacher = Teacher("teach1", "123456", "teacher1@gmail.com", "tea", "cher", "Male", datetime(2003, 12, 4), "D.Eng",
                  "Bangkok", "Thailand", "KMITL")
admin = Admin("admin", "admin1234", "admin1@gmail.com", "ad", "min", "Male", datetime(2003, 12, 4), "",
              "Bangkok", "Thailand")
student = Student("ffwatcharin", "firstbigdick", "ffwatcharin@gmail.com", "Watcharin", "Humthong", "Male",
                  datetime(2004, 1, 16), "Undergraduated", "Nonthaburi", "Thailand")

# --- Build Test --- #

course_system = CourseSystem()
course = Courses("SOFT001", "Object Oriented Programming", "Learn writing oop", "teach1", "Software", "All Ages",
                 "To understanding OOP", "10", "10", datetime.now(), "teacher1@gmail.com")
course2 = Courses("HARD001", "Basic Arduino", "Learn Basic Arduino", "teach1", "Hardware", "All Ages",
                  "To understanding Arduino", "10", "10", datetime.now(), "teacher1@gmail.com")
course3 = Courses("HARD002", "Circuits and Electronics", "Learn Circuit Electronic", "teach1", "Hardware", "All Ages",
                  "To understanding Arduino", "10", "10", datetime.now(), "teacher1@gmail.com")
course4 = Courses("SOFT002", "Programming Fundamentals", "Learn basic programming", "teach1", "Software", "All Ages",
                  "To understanding Arduino", "10", "10", datetime.now(), "teacher1@gmail.com")
course5 = Courses("MATH001", "Calculus I", "Learn Calculus I", "teach1", "Math", "All Ages",
                  "To understanding Arduino", "10", "10", datetime.now(), "teacher1@gmail.com")
course6 = Courses("MATH002", "Calculus II", "Learn Calculus II", "teach1", "Math", "All Ages",
                  "To understanding Arduino", "10", "10", datetime.now(), "teacher1@gmail.com")
course7 = Courses("MATH003", "Discrete Structure", "Learn Discrete math", "teach1", "Math", "All Ages",
                  "To understanding Arduino", "10", "10", datetime.now(), "teacher1@gmail.com")
course8 = Courses("SCI001", "Cellular Respiration", "Learn Cellular Respiration", "teach1", "Science", "All Ages",
                  "To understanding Arduino", "10", "10", datetime.now(), "teacher1@gmail.com")
course9 = Courses("SCI002", "Photosynthesis", "Learn Photosynthesis", "teach1", "Science", "All Ages",
                  "To understanding Arduino", "10", "10", datetime.now(), "teacher1@gmail.com")
course10 = Courses("MATH004", "Linear Algebra", "Learn Linear Algebra", "teach1", "Math", "All Ages",
                   "To understanding Linear Algebra", "10", "10", datetime.now(), "teacher1@gmail.com")
course11 = Courses("LAN001", "English for Communication", "Learn English for Communication", "teach1", "Language",
                   "All Ages",
                   "To understanding everyday English conversation", "10", "10", datetime.now(), "teacher1@gmail.com")
course12 = Courses("LAN002", "English for Business", "Learn English for Business", "teach1", "Language", "All Ages",
                   "To understanding Basic Business in English", "10", "10", datetime.now(), "teacher1@gmail.com")
course13 = Courses("LAN003", "Fundamental Chinese", "Learn Fundamental Chinese", "teach1", "Language", "All Ages",
                   "To understanding Basic Chinese", "10", "10", datetime.now(), "teacher1@gmail.com")
course14 = Courses("LAN004", "Fundamental Korean", "Learn Fundamental Korean", "teach1", "Language", "All Ages",
                   "To understanding Basic Korean", "10", "10", datetime.now(), "teacher1@gmail.com")
course15 = Courses("LAN005", "English for Marketing", "Learn English for Marketing", "teach1", "Language", "All Ages",
                   "To understanding Basic Marketing in English", "10", "10", datetime.now(), "teacher1@gmail.com")

# --- Build Test --- #
course_system.create_course(course)
course_system.create_course(course2)
course_system.create_course(course3)
course_system.create_course(course4)
course_system.create_course(course5)
course_system.create_course(course6)
course_system.create_course(course7)
course_system.create_course(course8)
course_system.create_course(course9)
course_system.create_course(course10)
course_system.create_course(course11)
course_system.create_course(course12)
course_system.create_course(course13)
course_system.create_course(course14)
course_system.create_course(course15)

course_system.add_user(teacher)
course_system.add_user(student)
course_system.add_user(admin)
print(course_system.get_user_db())

student.set_enrolled_course('enroll', course)  # Student has enrolled SOFT001.

oop_exam = CourseExam(course.get_title)
stu1doexam = CouseProgression(student.get_username, course.get_refcode)

# ------------------------------- API -----------------------------------#
app = FastAPI()


@app.get("/", tags=['root'])
async def root():
    return {"Welcome": "Hello World"}


# -------------------------------------------- User API -------------------------------------------- #
@app.get("/login", tags=["User API"])
async def login():
    pass


@app.get("/enrolled", tags=["User API"])
async def enrolled(username: str):
    u = course_system.search_user(username)
    return u.get_enrolled_course()


# ----------------------------------------- Course API ----------------------------------------- #
@app.get("/courses", tags=["Course API"])
async def courses():
    pass


# ------------------------------- Exam API --------------------------------#
@app.post("/exam/question and answer", tags=["Exam API"])
async def add_question(data: Problems):
    oop_exam.add_question_ans(data)
    course.set_exam(oop_exam)
    return {"Question and Answer added successfully"}


@app.put("/exam/edit", tags=["Exam API"])
async def update_exams(question_number: int, body: EditExam):
    return oop_exam.edit_exam(question_number, body.dict())


@app.get("/exam", tags=["Exam API"])
async def get_exam():
    return oop_exam.get_exams()


@app.post("/exam/do exam", tags=["Exam API"])
async def do_exam(data: list):
    stu1doexam.set_exam(oop_exam.get_exams())
    stu1doexam.do_exam(data)
    return {"successfully"}


@app.get("/exam/get progression", tags=["Exam API"])
async def get_progression():
    return {f'{stu1doexam.get_progress()} %'}


# -------------------------------- Enroll API ----------------------------- #
# Course Categories API #
@app.get("/coursescatg", tags=["Course Categories API"])
async def course_catg(data: str):
    print(course_system.browse_course(data))
    return course_system.browse_course(data)


# --- Enroll API --- #
@app.get("/cart", tags=["Enrollment"])
async def cart():
    return {"Cart": course_system.get_cart()}


@app.post("/addcart", tags=["Enrollment"])
async def add_cart(cart_item: dict) -> dict:
    username = cart_item["username"]
    refcode = cart_item["refcode"]

    print(username)
    print(refcode)

    u = course_system.search_user(username)
    c = course_system.search_course(refcode)

    print(u)
    print(c)
    if not course_system.add_cart(c, u.get_enrolled_course()):
        return {"Error": "Already enrolled! / Already in cart!"}
    else:
        course_system.add_cart(c, u.get_enrolled_course())
        return {"Cart": "Success"}


@app.post("/removecart", tags=["Enrollment"])
async def remove_cart(removal: dict) -> dict:
    refcode = removal["refcode"]
    print(refcode)
    c = course_system.search_course(refcode)
    if course_system.remove_cart(c):
        return {"Success": "Remove complete"}
    else:
        return {"Error": "No"}


@app.post("/enroll", tags=["Enrollment"])
async def enroll(user: str):
    u = course_system.search_user(user)
    if course_system.enroll(u):
        return {"Enroll": "Success"}
    else:
        return {"Enroll": "Cart is empty!"}


@app.post("/unenroll", tags=["Enrollment"])
async def unenroll(unenroll: dict) -> dict:
    username = unenroll["username"]
    refcode = unenroll["refcode"]
    u = course_system.search_user(username)
    c = course_system.search_course(refcode)
    if course_system.unenroll(u, c):
        return {"Unenroll": "Success"}
    else:
        return {"Unenroll": "Error"}
