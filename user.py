class UserData:
    def __init__(self):
        self.__user_data = []

    def get_user_db(self):
        return self.__user_data
    def delete_user(self):
        pass

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


class Admin(User):
    def __init__(self, username, password):
        User.__init__(self, username, password, user_type="Admin")


class Student(User):
    def __init__(self, username, password, email, fname, lname, gender, birth_date, education, province, country,
                 enrolled_course):
        User.__init__(self, username, password, email, fname, lname, gender, birth_date, education, province, country,
                      user_type="Student")
        self.__enrolled_course = enrolled_course


class Teacher(User):
    def __init__(self, username, password, email, fname, lname, gender, birth_date, education,
                 province, country, teacher_dept):
        User.__init__(self, username, password, email, fname, lname, gender, birth_date, education, province, country,
                      user_type="Teacher")
        self.__teacher_dept = teacher_dept
        self.__teached = []
