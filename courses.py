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
        self.__exam = None


    def get_refcode(self):
        return self.__refcode
    def get_catg(self):
        return self.__catg
    def get_title(self):
        return self.__title
    def set_exam(self,exam):
        self.__exam = exam

class CourseCatg:
    pass


# --- Course Material --- #
class CourseChapter:
    pass


class CourseMaterial:
    pass
