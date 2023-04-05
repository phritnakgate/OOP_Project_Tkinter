import datetime
from fastapi import *
from courses import *
from enroll import *

course_catalog = CourseCatalog()
cart = Cart()
# enroll = Enroll()
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

# --- Enroll API --- #
@app.get("/cart", tags=["Enroll System"])
async def cart():
    cart_data = cart.get_cart()
    return {"Cart": cart_data}
@app.post("/enroll", tags=["Enroll System"])
async def enroll():
    pass