import datetime
from fastapi import *
from courses import *

<<<<<<< Updated upstream
course_catalog = CourseCatalog()
=======
# enroll = Enroll()
>>>>>>> Stashed changes
app = FastAPI()


@app.get("/", tags=['root'])
async def root():
    return {"Welcome": "Hello World"}


# --- User API --- #
@app.post("/register", tags=['User CRUD'])
async def register():
    pass
@app.delete("/deluser", tags=['User CRUD'])
async def deluser():
    pass

<<<<<<< Updated upstream
# --- Course API --- #
@app.get("/courses", tags=['Course CRUD'])
async def courses():
    course_db = course_catalog.get_course()
    return {'All Courses': course_db}


@app.post("/create_course", tags=['Course CRUD'])
async def create_course(refcode: str, title: str, desc: str, teacher: str, catg: str, target: str, objective: str,
                        hour: str, recom_hour: str, contact: str):
    course_catalog.create_course(
        Courses(refcode, title, desc, teacher, catg, target, objective, hour, recom_hour, datetime.datetime.now(), contact))
    return {'Status': 'Success'}

@app.delete("/delcourse", tags=['Course CRUD'])
async def delete_course(refcode: str):
    course_catalog.delete_course(refcode)
    return {'Status': 'Success'}
=======

# --- Course API --- # 
@app.get("/courses", tags=["Course API"])
async def courses():
    pass

# --- Course Categories API --- #
@app.get("/coursescatg", tags=["Course Categories API"])
async def course_catg(data : str):  
    return  course_system.browse_course(data)
>>>>>>> Stashed changes
