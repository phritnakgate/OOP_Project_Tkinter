class UserData:
    def __init__(self):
        self.__user_data = []

    def get_user_db(self):
        return self.__user_data
    def register(self, created_user):
        self.__user_data.append(created_user)
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

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_email(self):
        return self.__email

    def get_fname(self):
        return self.__fname

    def get_lname(self):
        return self.__lname

    def get_gender(self):
        return self.__gender

    def get_birth_date(self):
        return self.__birth_date

    def get_education(self):
        return self.__education

    def get_province(self):
        return self.__province

    def get_country(self):
        return self.__country

    def get_user_type(self):
        return self.__user_type

class Admin(User):
    def __init__(self, username, password, email, fname, lname, gender, birth_date, education, province, country):
        User.__init__(self, username, password, email, fname, lname, gender, birth_date, education, province,
                      country, user_type="Admin")


class Student(User):
    def __init__(self, username, password, email, fname, lname, gender, birth_date, education, province, country):
        User.__init__(self, username, password, email, fname, lname, gender, birth_date, education, province, country,
                      user_type="Student")
        self.__enrolled_course = []


class Teacher(User):
    def __init__(self, username, password, email, fname, lname, gender, birth_date, education,
                 province, country, teacher_dept):
        User.__init__(self, username, password, email, fname, lname, gender, birth_date, education, province, country,
                      user_type="Teacher")
        self.__teacher_dept = teacher_dept
        self.__teached = []
