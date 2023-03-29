from user import *

class Cart:
    def __init__(self, enroll_course, user):
        self.enroll_course = enroll_course
        self.user = user

    def add_cart(self):
        pass

    def remove_cart(self):
        pass
class Enroll:
    def __init__(self):
        __user_db = UserDataBase()

    def check_enroll(self, will_enrolled, enrolled):
        if will_enrolled in enrolled:
            return False
        else:
            return True
