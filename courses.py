# --- Course Object --- #
class Courses:
    def __init__(self, refcode, title, desc, teacher, catg, target, objective, hour, recom_hour, release, contact):
        self.__refcode = refcode
        self.__title = title
        self.__desc = desc
        self.__teacher = teacher
        self.__catg = catg
        self.__target = target
        self.__objective = objective
        self.__hour = hour
        self.__recom_hour = recom_hour
        self.__release = release
        self.__contact = contact

    def get_catg(self):
        return self.__catg

    def get_title(self):
        return self.__title
    



# --- Course Material --- #
class CourseChapter:
    pass


class CourseMaterial:
    pass


class CourseExam:
    def __init__(self, course_name, exam_list, ans_list):
        self._course_name = course_name
        self._exam_list = exam_list
        self._ans_list = ans_list

    def do_exam(self):
        pass

    def ans_check(self):
        pass


class CouseProgression:
    def __init__(self):
        pass