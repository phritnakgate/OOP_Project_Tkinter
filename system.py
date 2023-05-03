from courses import *

class CourseSystem:
    def __init__(self):
        self.__course_list = []
        self.__user_list = []
        self.__cart = []

    # --------------- User --------------- #
    def add_user(self, user):
        self.__user_list.append(user)

    def get_user_db(self):
        return self.__user_list

    def delete_user(self,username):
        deluser_l = []
        for i in self.__user_list:
            deluser_l.append(i.get_username())
        try:
            del self.__user_list[deluser_l.index(username)]
        except:
            return False

    def search_user(self, name):
        username_l = []
        for u in self.__user_list:
            username_l.append(u.get_username())
        if name in username_l:
            return self.__user_list[username_l.index(name)]
        
    def login(self, username, password):
        try:
            user = self.search_user(username)
            if password == user.get_password():
                return True
            else:
                return False
        except:
            return False

    # --- Course --- #
    def create_course(self, created_course):
        self.__course_list.append(created_course)

    def get_all_course(self):
        return self.__course_list

    def delete_course(self, refcode):
        ref_l = []
        for i in self.__course_list:
            ref_l.append(i.get_refcode())

        try:
            del self.__course_list[ref_l.index(refcode)]
        except: return False

    def search_course(self, refcode):
        course_l = []
        for c in self.__course_list:
            course_l.append(c.get_refcode())
        if refcode in course_l:
            return self.__course_list[course_l.index(refcode)]

    def search_by_name(self,search_name):
        result = []
        for course in self.__course_list:
            if search_name.lower() in course.get_title().lower():
                result.append(course)
        if result: return result
        else: return {'Course Not Found!!'}
        
    def browse_course(self, catg):
        self.__coursecatg_list = []
        for i in self.__course_list:
            if i.get_catg() == catg:
                self.__coursecatg_list.append(i)
        return self.__coursecatg_list

    # --- Study --- #
    def get_course(self, user, refcode):
        u = self.search_user(user)
        ref = []
        for i in u.get_enrolled_course():
            ref.append(i.get_refcode())
        if refcode in ref:
            return u.get_enrolled_course()[ref.index(refcode)]
        else:
            return False

    def add_chapter(self, refcode, title):
        c = self.search_course(refcode)
        chap = CourseChapter(title)
        c.get_chapter().append(chap)

    def get_chapter(self, user, refcode, chapter):
        c = self.search_course(refcode)
        try:
            c.get_chapter()[int(chapter)]
        except:
            return {"ERROR": "Not found chapter"}
        return c.get_chapter()[int(chapter)]

    def get_material(self, refcode, chapter):
        c = self.search_course(refcode)
        return c.get_chapter()[int(chapter)].get_material()

    def add_material(self, refcode, chapter, material):
        c = self.search_course(refcode)
        c.get_chapter()[int(chapter)].get_material().append(material)

    def set_material(self, refcode, chapter, new):
        c = self.search_course(refcode)
        c.get_chapter()[int(chapter)].get_material()[0].edit_material(new)
        return c.get_chapter()[int(chapter)].get_material()


    # --- Enroll --- #
    def get_cart(self):
        return self.__cart

    def add_cart(self, will_enrolled, enrolled):
        if (will_enrolled in enrolled) or (will_enrolled in self.__cart):
            return False
        else:
            self.__cart.append(will_enrolled)
            return True

    def remove_cart(self, will_remove):
        if (will_remove in self.__cart) and (self.__cart != []):
            self.__cart.remove(will_remove)
            return True
        else:
            return False

    def enroll(self, user):
        if self.__cart:
            for i in self.__cart:
                user.set_enrolled_course('enroll', i)
            self.__cart = []
            return True
        else:
            return False

    def unenroll(self, user, course):
        er = user.get_enrolled_course()
        if course in er:
            er.remove(course)
            return True
        else:
            return False
