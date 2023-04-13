from courses import *
from datetime import *
from system import *

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
course11 = Courses("LAN001", "English for Communication", "Learn English for Communication", "teach1", "Language", "All Ages",
                 "To understanding everyday English conversation", "10", "10", datetime.now(), "teacher1@gmail.com")
course12= Courses("LAN002", "English for Business", "Learn English for Business", "teach1", "Language", "All Ages",
                 "To understanding Basic Business in English", "10", "10", datetime.now(), "teacher1@gmail.com")
course13= Courses("LAN003", "Fundamental Chinese", "Learn Fundamental Chinese", "teach1", "Language", "All Ages",
                 "To understanding Basic Chinese", "10", "10", datetime.now(), "teacher1@gmail.com")
course14= Courses("LAN004", "Fundamental Korean", "Learn Fundamental Korean", "teach1", "Language", "All Ages",
                 "To understanding Basic Korean", "10", "10", datetime.now(), "teacher1@gmail.com")
course15= Courses("LAN005", "English for Marketing", "Learn English for Marketing", "teach1", "Language", "All Ages",
                 "To understanding Basic Marketing in English", "10", "10", datetime.now(), "teacher1@gmail.com")

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
print(course_system.browse_course("Language"))