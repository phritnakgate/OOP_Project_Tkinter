class CourseSystem:
    def __init__(self):
        self.__course_list = []
        self.__user_list = []

    def add_user(self, user):
        self.__user_list.append(user)

    def delete_user(self):
        pass

    def search_user(self, name):
        for u in self.__user_list:
            if u.name == name:
                return u

    def create_course(self, created_course):
        self.__course_list.append(created_course)

    def get_course(self):
        return self.__course_list

    def modify_course(self):
        pass

    def delete_course(self, refcode):
        pass

