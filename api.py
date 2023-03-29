from fastapi import *
import json


user_file = open('userdata.json')
user_db = json.load(user_file)

course_file = open('coursedata.json')
course_db = json.load()

fapi = FastAPI()

# --------------------------------- User API --------------------------------- #
@fapi.get("/getuserdb")
async def get_user_db():
    return user_db

@fapi.post("/register")
async def register():
    pass

# --------------------------------- Course API --------------------------------- #
@fapi.get("/getcoursedb")
async def get_course_db():
    pass