from review import Review
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
        self.__chapter = []
        self.__review = []
        self.__review_score = 0

    def get_refcode(self):
        return self.__refcode
    
    def get_title(self):
        return self.__title
    
    def get_desc(self):
        return self.__desc
    
    def get_teacher(self):
        return self.__teacher
    
    def get_catg(self):
        return self.__catg
    
    def get_target(self):
        return self.__target
    
    def get_objective(self):
        return self.__objective
    
    def get_hour(self):
        return self.__hour
    
    def get_recom_hour(self):
        return self.__recom_hour
    
    def get_release(self):
        return self.__release
    
    def get_contact(self):
        return self.__contact

    def set_exam(self, exam):
        self.__exam = exam
        
    def get_exam(self):
        return self.__exam    

    def set_chapter(self, chapter):
        self.__chapter.append(chapter)

    def get_chapter(self):
        return self.__chapter
    
    def get_review(self):
        return self.__review
    
    def get_review_score(self):
        return self.__review_score
    
    def set_review(self, review:Review):
        self.__review.append(review)
        self.__review_score = sum([i.get_write_review () for i in self.__review])/len(self.__review)

# --- Course Material --- #
class CourseChapter:
    def __init__(self, title):
        self.__title = title
        self.__material = []

    def get_material(self):
        return self.__material

    def set_material(self, material):
        self.__material.append(material)

class CourseMaterial:
    def __init__(self, material):
        self.__material = material

    def edit_material(self, new):
        self.__material = new