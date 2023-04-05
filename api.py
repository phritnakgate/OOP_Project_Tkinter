import datetime
from fastapi import *
from courses import *
from enroll import *
from system import *

course_catalog = CourseSystem()
cart = Cart()
# enroll = Enroll()
app = FastAPI()


@app.get("/", tags=['root'])
async def root():
    return {"Welcome": "Hello World"}


# --- User API --- #
@app.get("/login", tags=["User API"])
async def login():
    pass


# --- Course API --- #
@app.get("/courses", tags=["Course API"])
async def courses():
    pass