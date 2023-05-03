from fastapi import FastAPI
from user import *
from system import *
from datetime import datetime
from courses import *
from exam import *
from dto import *

# --- Creation Test --- #
teacher1 = Teacher("teach1", "123456", "teacher1@gmail.com", "tea", "cher", "Male", datetime(2003, 12, 4), "D.Eng",
                   "Bangkok", "Thailand", "KMITL")
admin = Admin("admin", "admin1234", "admin1@gmail.com", "ad", "min", "Male", datetime(2003, 12, 4), "",
              "Bangkok", "Thailand")
student = Student("ffwatcharin", "firstbigdick", "ffwatcharin@gmail.com", "Watcharin", "Humthong", "Male",
                  datetime(2004, 1, 16), "Undergraduated", "Nonthaburi", "Thailand")
testdel = Student("del", "del", "eiei@gmail.com", "d", "d", "Male",
                  datetime(2003, 12, 4), "Undergraduated", "Nonthaburi", "Thailand")

# --- Build Test --- #

course_system = CourseSystem()
course = Courses("SOFT001", "Object Oriented Programming", "Learn writing oop", "teach1", "Software", "All Ages",
                 "To understanding OOP", "10", "10", datetime.now(), "teacher1@gmail.com")
course.set_exam(CourseExam(course.get_refcode()))

course2 = Courses("HARD001", "Basic Arduino", "Learn Basic Arduino", "teach1", "Hardware", "All Ages",
                  "To understand Arduino", "10", "10", datetime.now(), "teacher1@gmail.com")
course2.set_exam(CourseExam(course2.get_refcode()))

course3 = Courses("HARD002", "Circuits and Electronics", "Learn Circuit Electronic", "teach1", "Hardware", "All Ages",
                  "To understand electronic circuits", "10", "10", datetime.now(), "teacher1@gmail.com")
course3.set_exam(CourseExam(course3.get_refcode()))

course4 = Courses("SOFT002", "Programming Fundamentals", "Learn basic programming", "teach1", "Software", "All Ages",
                  "To understand Programming Fundamentals", "10", "10", datetime.now(), "teacher1@gmail.com")
course4.set_exam(CourseExam(course4.get_refcode()))

course5 = Courses("MATH001", "Calculus I", "Learn Calculus I", "teach1", "Math", "All Ages",
                  "To understand Calculus I", "10", "10", datetime.now(), "teacher1@gmail.com")
course5.set_exam(CourseExam(course5.get_refcode()))

course6 = Courses("MATH002", "Calculus II", "Learn Calculus II", "teach1", "Math", "All Ages",
                  "To understand Calculus II", "10", "10", datetime.now(), "teacher1@gmail.com")
course6.set_exam(CourseExam(course6.get_refcode()))

course7 = Courses("MATH003", "Discrete Structure", "Learn Discrete math", "teach1", "Math", "All Ages",
                  "To understand discrete math", "10", "10", datetime.now(), "teacher1@gmail.com")
course8 = Courses("SCI001", "Cellular Respiration", "Learn Cellular Respiration", "teach1", "Science", "All Ages",
                  "To understand cellular respirarion", "10", "10", datetime.now(), "teacher1@gmail.com")
course9 = Courses("SCI002", "Photosynthesis", "Learn Photosynthesis", "teach1", "Science", "All Ages",
                  "To understand photosynthesis", "10", "10", datetime.now(), "teacher1@gmail.com")
course10 = Courses("MATH004", "Linear Algebra", "Learn Linear Algebra", "teach1", "Math", "All Ages",
                   "To understand Linear Algebra", "10", "10", datetime.now(), "teacher1@gmail.com")
course11 = Courses("LAN001", "English for Communication", "Learn English for Communication", "teach1", "Language",
                   "All Ages", "To understand everyday English conversation", "10", "10", datetime.now(), "teacher1@gmail.com")
course12 = Courses("LAN002", "English for Business", "Learn English for Business", "teach1", "Language", "All Ages",
                   "To understand Basic Business in English", "10", "10", datetime.now(), "teacher1@gmail.com")
course13 = Courses("LAN003", "Fundamental Chinese", "Learn Fundamental Chinese", "teach1", "Language", "All Ages",
                   "To understand Basic Chinese", "10", "10", datetime.now(), "teacher1@gmail.com")
course14 = Courses("LAN004", "Fundamental Korean", "Learn Fundamental Korean", "teach1", "Language", "All Ages",
                   "To understand Basic Korean", "10", "10", datetime.now(), "teacher1@gmail.com")
course15 = Courses("LAN005", "English for Marketing", "Learn English for Marketing", "teach1", "Language", "All Ages",
                   "To understand Basic Marketing in English", "10", "10", datetime.now(), "teacher1@gmail.com")

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

course_system.add_user(teacher1)
course_system.add_user(student)
course_system.add_user(testdel)
course_system.add_user(admin)
print(course_system.get_user_db())

student.set_enrolled_course('enroll', course)  # Student has enrolled SOFT001.

# SOFT001 Chapter
course_system.add_chapter('SOFT001', '01:Basic Python')
chap1_mat = CourseMaterial(
    "https://www.youtube.com/watch?v=N1fnq4MF3AE&list=PLltVQYLz1BMBwqJysYnoEKWXUvqusJpgN&ab_channel=KongRuksiam")
course_system.add_material('SOFT001', 0, chap1_mat)

course_system.add_chapter('SOFT001', '02:Intermediate Python')
chap2_mat = CourseMaterial(
    "https://www.youtube.com/watch?v=N1fnq4MF3AE&list=PLltVQYLz1BMBwqJysYnoEKWXUvqusJpgN&ab_channel=KongRuksiam")
course_system.add_material('SOFT001', 1, chap2_mat)

course_system.add_chapter('SOFT001', '03:OOP Principle')
chap3_mat = CourseMaterial("OOP is Object Oriented Programming")
course_system.add_material('SOFT001', 2, chap3_mat)

# ------------------------------- API -----------------------------------#
app = FastAPI()

@app.get("/", tags=['root'])
async def root():
    return {"Welcome": "Hello OOP"}

# -------------------------------------------- User API -------------------------------------------- #
# register
@app.post("/register", tags=["User API"])
async def register(form_data: dict):
    username = form_data["username"]
    password = form_data["password"]
    email = form_data["email"]
    fname = form_data["fname"]
    lname = form_data["lname"]
    gender = form_data["gender"]
    birth_date = form_data["birth_date"]
    education = form_data["education"]
    province = form_data["province"]
    country = form_data["country"]
    user_type = form_data["user_type"]

    if user_type == "Teacher":
        teacher_dept = form_data["teacher_dept"]
        course_system.add_user(
            Teacher(username=username, password=password, email=email, fname=fname, lname=lname, gender=gender,
                    birth_date=birth_date, education=education, province=province,
                    country=country, teacher_dept=teacher_dept))
        return {"message": "teacher created"}
    elif user_type == "Student":
        course_system.add_user(
            Student(username=username, password=password, email=email, fname=fname, lname=lname, gender=gender,
                    birth_date=birth_date, education=education, province=province,
                    country=country))
        return {"message": "student created"}
    elif user_type == "Admin":
        course_system.add_user(
            Admin(username=username, password=password, email=email, fname=fname, lname=lname, gender=gender,
                  birth_date=birth_date, education=education, province=province,
                  country=country))
        return {"message": "admin created"}


# login
@app.post("/login", tags=["User API"])
async def login(username: str, password: str):
    if course_system.login(username, password):
        return {"Status": "Login Success!",
                "username": username,
                "password": password,
                "user_type": course_system.search_user(username).get_user_type()}
    else:
        return {"Status": "Username/Password Incorrect!!"}


# modify user
@app.put("/update_user/{username}", tags=["User API"])
async def update_user(username: str, form_data: dict):
    user = course_system.search_user(username)
    if user is None:
        return {"message": "User not found"}

    if "password" in form_data:
        user._User__password = form_data["password"]
    if "email" in form_data:
        user._User__email = (form_data["email"])
    if "fname" in form_data:
        user._User__fname = form_data["fname"]
    if "lname" in form_data:
        user._User__lname = form_data["lname"]
    if "gender" in form_data:
        user._User__gender = form_data["gender"]
    if "birth_date" in form_data:
        user._User__birth_date = form_data["birth_date"]
    if "education" in form_data:
        user._User__education = form_data["education"]
    if "province" in form_data:
        user._User__province = form_data["province"]
    if "country" in form_data:
        user._User__country = form_data["country"]
    if user.get_user_type() == "Teacher" and "teacher_dept" in form_data:
        user._Teacher__teacher_dept = form_data["teacher_dept"]
    return {"message": "User information updated successfully"}


# delete user
@app.delete("/delete_user", tags=["User API"])
async def delete_user(username: str):
    course_system.delete_user(username)
    return {"message": "Username has been deleted"}


# check create users
@app.get("/all_users", tags=["User API"])
async def read_users():
    return course_system.get_user_db()


@app.get("/users/{username}", tags=["User API"])
async def get_user(username):
    return course_system.search_user(username)


@app.get("/enrolled", tags=["User API"])
async def enrolled(username: str):
    u = course_system.search_user(username)
    return u.get_enrolled_course()


# ----------------------------------------- Course API ----------------------------------------- #
@app.get("/courses", tags=["Course API"])
async def courses():
    return course_system.get_all_course()


@app.get("/courses/{refcode}", tags=["Course API"])
async def get_by_refcode(refcode):
    return course_system.search_course(refcode)


@app.post("/create_course", tags=["Course API"])
async def create_course(course_info: dict):
    refcode = course_info["refcode"]
    title = course_info["title"]
    desc = course_info["desc"]
    teacher = course_info["teacher"]
    catg = course_info["catg"]
    target = course_info["target"]
    objective = course_info["objective"]
    hour = course_info["hour"]
    recom_hour = course_info["recom_hour"]
    release = datetime.now()
    contact = course_info["contact"]

    ccourse = Courses(refcode=refcode, title=title, desc=desc, teacher=teacher, catg=catg, target=target,
                      objective=objective, hour=hour, recom_hour=recom_hour, release=release, contact=contact)
    ccourse.set_exam(CourseExam(title))
    course_system.create_course(ccourse)

    return {
        "message": "course created"
    }

@app.delete("/delete_course", tags=["Course API"])
async def delete_course(refcode: str):
    course_system.delete_course(refcode)


@app.get("/courses/search_by_name", tags=["Course API"])
async def search_name(data: str):
    return course_system.search_by_name(data)


# Course Categories API #
@app.get("/courses/category/{catg}", tags=["Course Categories API"])
async def course_catg(catg):
    data = course_system.browse_course(catg)
    return data

@app.get("/courses/{user}/{refcode}", tags=["Course API"])
async def get_course(user, refcode):
    if course_system.get_course(user, refcode):
        return course_system.get_course(user, refcode)
    else:
        return {"Error": "Not enrolled!"}


@app.get("/courses/{user}/{refcode}/{chapter}", tags=["Course API"])
async def get_chapter(user, refcode, chapter):
    return course_system.get_chapter(user, refcode, chapter)

@app.put("/courses/{refcode}/{chapter}/modify", tags=["Course API"])
async def modify_chapter(refcode, chapter, newmat: str):
    return course_system.set_material(refcode, chapter, newmat)

@app.post("/courses/{refcode}/create_chapter", tags=["Course API"])
async def create_chapter(refcode, titles:list, materials:list):
    courses = course_system.search_course(refcode)    
    for i in range(len(titles)):
        title = titles[i]
        material = materials[i]
        chapter = CourseChapter(title)
        chapter.set_material(CourseMaterial(material))
        courses.set_chapter(chapter)

@app.post("/add_review", tags=["Course API"])
async def add_review(data: AddReviewDTO):
    courses = course_system.search_course(data.refcode)
    courses.set_review(Review(data.user, data.score, data.comment))
    return {"status": "Add Success"}


@app.get("/{refcode}/reviews", tags=["Course API"])
async def get_review(refcode):
    return course_system.search_course(refcode).get_review()


# ------------------------------- Exam API --------------------------------#
@app.post("/exam/question_and_answer", tags=["Exam API"])
async def add_question(refcode:str ,data: QuestListDTO):  
    course = course_system.search_course(refcode)  
    if course == None:
        return {"Refcode not found"}
    else:
        exams = course.get_exam()   
        exams.add_question_ans(data)
        return {"Add Successfully"}


@app.put("/{refcode}/exam/edit", tags=["Exam API"])
async def update_exams(refcode:str,question_number: int, body: EditExamDTO):
    course = course_system.search_course(refcode)  
    exams = course.get_exam()
    return exams.edit_exam(question_number, body.dict())


@app.get("/exam", tags=["Exam API"])
async def get_exam(refcode:str):
    course = course_system.search_course(refcode)  
    exams = course.get_exam() 
    return exams.get_exams()


@app.post("/courses/{user}/{refcode}/exam/do_exam", tags=["Exam API"])
async def do_exam(refcode,user,data: list):
    course = course_system.search_course(refcode)  
    exams = course.get_exam() 
    studoexam = CourseProgression(user, refcode)
    studoexam.set_exam(exams.get_exams())
    studoexam.do_exam(data)    
    users = course_system.search_user(user)
    users.set_progression(studoexam)
    return {f'{studoexam.get_progress()} %'}

@app.get("/{user}/get_all_grogression", tags=["Exam API"])
async def get_all_progression(user):
    users = course_system.search_user(user)
    print(users)
    return users.get_progression()

# -------------------------------- Enroll API ----------------------------- #
@app.get("/cart", tags=["Enrollment"])
async def cart():
    return {"Cart": course_system.get_cart()}


@app.post("/addcart", tags=["Enrollment"])
async def add_cart(cart_item: dict) -> dict:
    username = cart_item["username"]
    refcode = cart_item["refcode"]

    # print(username)
    # print(refcode)

    u = course_system.search_user(username)
    c = course_system.search_course(refcode)

    # print(u)
    # print(c)
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
