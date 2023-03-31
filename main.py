import requests
from datetime import datetime
from courses import *
from user import *

teacher = Teacher("teach1", "123456", "teacher1@gmail.com", "tea", "cher", "Male", datetime(2003, 12, 4), "D.Eng",
                  "Bangkok", "Thailand", "KMITL")
course = Courses("SOFT001", "Object Oriented Programming", "Learn writing oop", "teach1", "Software", "All Ages",
                 "To understanding OOP", "10", "10", datetime.now(), "teacher1@gmail.com")

course_cata = CourseCatalog()
course_cata.create_course(course)
all = course_cata.get_course()
print(all)
print(all[0].get_refcode())
print(all[0].get_title())

# --- API Test --- #
#r = requests.post('http://localhost:8000/create_course', data=course)
