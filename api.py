from fastapi import *
import json


f = open('userdata.json')
user_db = json.load(f)

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