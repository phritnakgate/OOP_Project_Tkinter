class Course:
    def __init__(self, course_name, course_teacher, course_catg):
        self.__course_name = course_name
        self.__course_teacher = course_teacher
        self.__course_catg = course_catg
    def create_course(self):
        print("Successfully created", self.__course_name)
        return [self.__course_name, self.__course_teacher]

class CourseCatalog:
    def __init__(self):
        self._catalog = [["Basic C Programming", "Thanunchai", "Software"],
                        ["Object Oriented Programming", "Thana", "Software"]
                        ]
    def add_course_to_catalog(self, course):
        self._catalog.append(course)
        print(self._catalog)
    def get_course_catalog(self):
        return self._catalog

class CourseCatg:
    def __init__(self):
        pass

class CourseRecom:
    def __init__(self):
        pass