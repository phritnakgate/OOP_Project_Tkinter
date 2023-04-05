<<<<<<< Updated upstream
class UserDataBase:
    def __init__(self):
        # User Database : [username, password, firstname, lastname, usertype, enrolled, teach(if teacher)]
        self._user_data = [['ffwatcharin', 'firstbigdick' ,'Watcharin', 'Humthong', 'User', []],
                          ['thana.h', '123456' , 'Thana', 'Hongsuwan', 'Teacher', [], ['OOP']],
                          ['thanunchi.t', '123456', 'Thanunchai', 'Treepak', 'Teacher', [], ['Discrete']],
                          ['admin', 'admin1234', '', '', 'Admin', [], []],
                           ['del', 'del']
                            ]

    def add_user_to_db(self, created_user):
        self._user_data.append(created_user)

    def get_user_db(self):
        return self._user_data

class User:
    def __init__(self):
        _user_db = UserDataBase()
        self._enrolled_course = []
        self._teach = []
        self._user_db = _user_db.get_user_db()

    # --------------------------------- User CRUD --------------------------------- #
    def register(self, username, password, first_name, last_name, user_type):
        if user_type == "User":
            return [username, password, first_name, last_name, user_type, self._enrolled_course]
        elif user_type == "Teacher":
            return [username, password, first_name, last_name, user_type, self._enrolled_course, self._teach]
        elif user_type == "Admin":
            return [username, password, "admin", "admin", user_type, self._enrolled_course, self._teach]

    def delete_user(self,username):
        if self.check_valid_username(username) != -1:
            del self._user_db[self.check_valid_username(username)]
            print(self._user_db)
            return True
        else:
            return False

    def modify_user(self):
        pass
    # --------------------------------- Check Validity --------------------------------- #
    def check_valid(self, username, password):
        username_list = []
        for i in range(len(self._user_db)):
            username_list.append(self._user_db[i][0])
        print(username_list)
        if username in username_list:
            if password == self._user_db[username_list.index(username)][1]:
                return True
            else:
                return False
        else:
            return False

    def check_valid_username(self, username):
        username_list = []
        for i in range(len(self._user_db)):
            username_list.append(self._user_db[i][0])
        if username in username_list:
            return username_list.index(username)
        else:
            return -1

=======
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
        self._enrolled_course = []       
    
    def get_enrolled_course(self):
        return self._enrolled_course

    def set_enrolled_course(self, request, will_enroll):
        if request == 'enroll':
            self._enrolled_course.append(will_enroll)
        elif request == 'unenroll':
            self._enrolled_course.remove(will_enroll)
            
    def enroll_course(self, course):
        self._enrolled_course.append(course)
                

class Teacher(User):
    def __init__(self, username, password, email, fname, lname, gender, birth_date, education,
                 province, country, teacher_dept):
        User.__init__(self, username, password, email, fname, lname, gender, birth_date, education, province, country,
                      user_type="Teacher")
        self.__teacher_dept = teacher_dept
        self.__teached = []
>>>>>>> Stashed changes
