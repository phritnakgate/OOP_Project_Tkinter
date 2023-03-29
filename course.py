class Course:
    def __init__(self):
        self.review = []
    def create_course(self, Refcode, Name, Teacher, Course_Category):
        print("Successfully created", Name)
        return [Refcode, Name, Teacher, Course_Category, [], []]
    def delete_course(self):
        pass

class CourseCatalog:
    def __init__(self):
        # Catalog: [Refcode, Name, Teacher, Course_Category, CourseMaterial(Chapter,[Material]), [Review]]
        self._catalog = [["SOFT001", "Basic C Programming", "Thanunchai", "Software", [["Ch1:Intro to C", []], ["Ch2:Basic I/O", []]]],
                        ["SOFT002", "Object Oriented Programming", "Thana", "Software", [["Ch1:Intro to OOP", []]]]
                        ]

    def add_course_to_catalog(self, course):
        self._catalog.append(course)
        print(self._catalog)

    def get_course_catalog(self):
        return self._catalog

    def get_course(self):
        pass
class CourseCatg:
    def __init__(self):
        pass

class CourseRecom:
    def __init__(self):
        pass

class CourseChapter:
    def __init__(self):
        __course_mat = CourseMaterial()
        self._chapter = []
    def add_chapter(self,chap_name):
        self._chapter.append([chap_name, []])
    def get_chapter(self):
        pass
class CourseMaterial:
    def __init__(self):
        self._material = []

    def add_material(self, mat):
        self._material.append(mat)

    def get_material(self, chapter):
        pass
class CourseExam:
    def __init__(self):
        pass

class CouseProgression:
    def __init__(self):
        pass

class Review:
    def __init__(self):
        pass