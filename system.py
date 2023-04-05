class CourseSystem:
    def __init__(self):
        self.__course_list = []
        self.__user_list = []
        self.__cart = []

    # --- User --- #
    def add_user(self, user):
        self.__user_list.append(user)
    def get_user_db(self):
        return self.__user_list
    def delete_user(self):
        pass

    def search_user(self, name):
        username_l = []
        for u in self.__user_list:
            username_l.append(u.get_username())
        if name in username_l:
            return self.__user_list[username_l.index(name)]

    # --- Course --- #
    def create_course(self, created_course):
        self.__course_list.append(created_course)

    def get_course(self):
        return self.__course_list

    def modify_course(self):
        pass

    def delete_course(self, refcode):
        pass
    def search_course(self, name):
        course_l = []
        for c in self.__course_list:
            course_l.append(c.get_refcode())
        if name in course_l:
            return self.__course_list[course_l.index(name)]
    # --- Enroll --- #
    def get_cart(self):
        return self.__cart
    def add_cart(self, will_enrolled, enrolled):
        if will_enrolled in enrolled:
            return False
        else:
            self.__cart.append(will_enrolled)
    def enroll(self, user, cart):
        for i in cart:
            user.set_enrolled_course('enroll', i)
        self.__cart = []

