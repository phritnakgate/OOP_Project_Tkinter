from user import *
from course import *
from ui import *

LoginUI()

"""
# --------------------------------- User_Creation --------------------------------- #
userdb = UserDataBase()

user1 = User("Watcharin", "Humthong", "User")
userdb.add_user_to_db(user1.create_user())

user2 = User("Thana", "Hongsuwan", "Teacher")
user2.teach.append("OOP")
userdb.add_user_to_db(user2.create_user())

user3 = User("Thanunchai", "Treepak", "Teacher")
user3.teach.append("Discrete")
userdb.add_user_to_db(user3.create_user())

# --------------------------------- Course_Creation --------------------------------- #
cata = CourseCatalog()

c1 = Course("OOP", user2.first_name)
c1_m = c1.create_course()
cata.add_course_to_catalog(c1_m)

c2 = Course("Discrete", user3.first_name)
c2_m = c2.create_course()
cata.add_course_to_catalog(c2_m)

# --------------------------------- Check --------------------------------- #
"""
