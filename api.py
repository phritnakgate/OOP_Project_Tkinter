import datetime
from fastapi import *
from courses import *
from enroll import *
from system import *
from user import *


course_catalog = CourseSystem()
cart = Cart()
# enroll = Enroll()
app = FastAPI()


@app.get("/", tags=['root'])
async def root():
    return {"Welcome": "Hello World"}


# --- User API --- #

#register
@app.post("/register", tags=["User API"])
async def register(form_data: dict):
    username = form_data["username"]
    password = form_data["password"]

    course_catalog.add_user(User(username=username, password=password))
    return {
        "messsage": "user created"
    }
#check create users
@app.get("/users", tags=["User API"])
async def read_users():
    return course_catalog.get_users()


@app.get("/login", tags=["User API"])
async def login():
    pass

# --- Course API --- #
@app.get("/courses", tags=["Course API"])
async def courses():
    pass