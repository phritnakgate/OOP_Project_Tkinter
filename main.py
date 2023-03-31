import requests
from datetime import datetime
from courses import *
from user import *

teacher = Teacher("teach1", "123456", "teacher1@gmail.com", "tea", "cher", "Male", datetime(2003, 12, 4), "D.Eng",
                  "Bangkok", "Thailand", "KMITL")
admin = Admin("admin", "admin1234", "admin1@gmail.com", "ad", "min", "Male", datetime(2003, 12, 4), "",
                  "Bangkok", "Thailand")
student = Student("ffwatcharin", "firstbigdick", "ffwatcharin@gmail.com", "Watcharin", "Humthong", "Male",
                  datetime(2004, 1, 16), "Undergraduated","Nonthaburi", "Thailand")

course = Courses("SOFT001", "Object Oriented Programming", "Learn writing oop", "teach1", "Software", "All Ages",
                 "To understanding OOP", "10", "10", datetime.now(), "teacher1@gmail.com")

course_cata = CourseCatalog()
userdb = UserData()

course_cata.create_course(course)
userdb.register(teacher)
userdb.register(admin)

all = course_cata.get_course()
all_u = userdb.get_user_db()
print(all)
print(all_u)
print(all[0].get_refcode())
print(all[0].get_title())

# --- API Test --- #
#r = requests.post('http://localhost:8000/create_course', data=course)
