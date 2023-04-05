import requests
from datetime import datetime
from courses import *
from user import *
from enroll import *

# --- Creation Test --- #
teacher = Teacher("teach1", "123456", "teacher1@gmail.com", "tea", "cher", "Male", datetime(2003, 12, 4), "D.Eng",
                  "Bangkok", "Thailand", "KMITL")
admin = Admin("admin", "admin1234", "admin1@gmail.com", "ad", "min", "Male", datetime(2003, 12, 4), "",
                  "Bangkok", "Thailand")
student = Student("ffwatcharin", "firstbigdick", "ffwatcharin@gmail.com", "Watcharin", "Humthong", "Male",
                  datetime(2004, 1, 16), "Undergraduated","Nonthaburi", "Thailand")

course = Courses("SOFT001", "Object Oriented Programming", "Learn writing oop", "teach1", "Software", "All Ages",
                 "To understanding OOP", "10", "10", datetime.now(), "teacher1@gmail.com")
course2 = Courses("HARD001", "Basic Arduino", "Learn Basic Arduino", "teach1", "Hardware", "All Ages",
                 "To understanding Arduino", "10", "10", datetime.now(), "teacher1@gmail.com")
# --- Build Test --- #
course_system = CourseSystem()
cart = Cart()

course_system.create_course(course)
course_system.create_course(course2)

# --- Enroll Test --- #
student.set_enrolled_course('enroll', course)
print(student.get_enrolled_course())

enroll2 = Enroll(course2, student.get_enrolled_course())
print(enroll2.check_enroll())

if enroll2.check_enroll() == True:
    cart.add_cart(course2)

print(cart.get_cart())
cart.enrolled(student, cart.get_cart())
print(student.get_enrolled_course())

# --- Getter/Setter Test --- #
# all = course_cata.get_course()
# all_u = userdb.get_user_db()
# print(all)
# print(all_u)
# print(all[0].get_refcode())
# print(all[0].get_title())


# --- API Test --- #
#r = requests.post('http://localhost:8000/create_course', data=course)
