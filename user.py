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
        username_list = []
        for i in range(len(self._user_db)):
            username_list.append(self._user_db[i][0])
        if user_type == "User" and username not in username_list:
            return [username, password, first_name, last_name, user_type, self._enrolled_course]
        elif user_type == "Teacher" and username not in username_list:
            return [username, password, first_name, last_name, user_type, self._enrolled_course, self._teach]
        elif user_type == "Admin" and username not in username_list:
            return [username, password, "admin", "admin", user_type, self._enrolled_course, self._teach]
        else:
            return []
    def delete_user(self, username):
        if self.check_valid_username(username) != -1:
            del self._user_db[self.check_valid_username(username)]
            print(self._user_db)
            return True
        else:
            return False

    def modify_user(self, username, password, first_name, last_name):
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

