from tkinter import *
from tkinter.font import *
import tkinter.messagebox
import requests
import json

class CourseCatalog:
    def __init__(self, username):
        self.__username = username
        self.__all_course = []
        self.__total_course = 0
        self.__row_base = 1
        # ------ Create GUI ------ #
        self.__catalog = Tk()
        self.__header_font = Font(family="Kanit", weight="bold", size=20)
        self.__normal_font = Font(family="Kanit", weight="normal", size=16)
        self.__txtbox_font = Font(family="Kanit", weight="normal", size=12)
        self.__catalog.title("CE MOOC")
        self.__catalog.geometry("1000x1000")
        self.__catalog.resizable(width=False, height=False)
        Label(text="Welcome To CE MOOC", font=self.__header_font).grid(row=0, column=1)
        self.get_all_course()
        for i in range(0, self.__total_course, 3):
            # -- Future Code: When total course %3 != 0 -- #
            if self.__total_course % 3 == 0:
                for j in range(3):
                    Label(text=self.__all_course[i+j]['_Courses__refcode'], font=self.__normal_font).grid(row=self.__row_base, column=j)
                    Label(text=self.__all_course[i+j]['_Courses__title'], font=self.__normal_font).grid(row=self.__row_base+1, column=j)
            self.__row_base +=2
        self.__catalog.mainloop()
    def get_all_course(self):
        r = requests.get("http://localhost:8000/courses")
        data = json.loads(r.text)
        self.__total_course = len(data)
        for i in data:
            self.__all_course.append(i)

CourseCatalog("Guest").get_all_course()