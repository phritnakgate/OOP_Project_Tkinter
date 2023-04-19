class User:
    def __init__(self, username, password, email, fname, lname, gender, birth_date, education, province, country,
                 user_type):
        self.__username = username
        self.__password = password
        self.__email = email
        self.__fname = fname
        self.__lname = lname
        self.__gender = gender
        self.__birth_date = birth_date
        self.__education = education
        self.__province = province
        self.__country = country
        self.__user_type = user_type

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_user_type(self):
        return self.__user_type


class Admin(User):
    def __init__(self, username, password, email, fname, lname, gender, birth_date, education, province, country):
        User.__init__(self, username, password, email, fname, lname, gender, birth_date, education, province,
                      country, user_type="Admin")

    def get_username(self):
        return super().get_username()


class Student(User):
    def __init__(self, username, password, email, fname, lname, gender, birth_date, education, province, country):
        User.__init__(self, username, password, email, fname, lname, gender, birth_date, education, province, country,
                      user_type="Student")
        self._enrolled_course = []

    def get_username(self):
        return super().get_username()

    def get_enrolled_course(self):
        return self._enrolled_course

    def set_enrolled_course(self, request, will_enroll):
        if request == 'enroll':
            self._enrolled_course.append(will_enroll)
        elif request == 'unenroll':
            self._enrolled_course.remove(will_enroll)


class Teacher(User):
    def __init__(self, username, password, email, fname, lname, gender, birth_date, education,
                 province, country, teacher_dept):
        User.__init__(self, username, password, email, fname, lname, gender, birth_date, education, province, country,
                      user_type="Teacher")
        self.__teacher_dept = teacher_dept
        self.__teached = []

    def get_username(self):
        return super().get_username()
