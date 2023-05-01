import customtkinter as ctk
import requests
import json
from functools import partial

from gui.editexamgui import ExamEditor
from gui.editmaterial import EditMaterial

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class TeacherDashboard:
    def __init__(self, user):
        self.__username = user
        self.__teached_refcode = []
        self.__teached_title = []
        self.__posy = 100
        self.__tdash = ctk.CTk()
        self.__header_font = ctk.CTkFont(family="Kanit", weight="bold", size=20)
        self.__normal_font = ctk.CTkFont(family="Kanit", weight="normal", size=16)
        self.__txtbox_font = ctk.CTkFont(family="Kanit", weight="normal", size=12)
        self.__tdash.title("Teacher Dashboard")
        self.__tdash.geometry("900x900")
        ctk.CTkLabel(self.__tdash, text="Teacher Dashboard", font=self.__header_font).pack()
        ctk.CTkButton(self.__tdash, text="Teach New Course", font=self.__txtbox_font).pack()
        self.check_teached_course()
        for i in range(len(self.__teached_refcode)):
            ctk.CTkLabel(self.__tdash, text=self.__teached_refcode[i]+":"+self.__teached_title[i], font=self.__normal_font).place(x=50, y=self.__posy)
            ctk.CTkButton(self.__tdash, text="Modify Detail", font=self.__txtbox_font,
                          command=partial(self.modify_course_detail, self.__teached_refcode[i])).place(x=400, y=self.__posy)
            ctk.CTkButton(self.__tdash, text="Modify Material", font=self.__txtbox_font,
                          command=partial(self.modify_course_material, self.__teached_refcode[i])).place(x=550, y=self.__posy)
            ctk.CTkButton(self.__tdash, text="Modify Exam", font=self.__txtbox_font,
                          command=partial(self.modify_course_exam, self.__teached_refcode[i])).place(x=700, y=self.__posy)
            self.__posy += 50
        self.__tdash.mainloop()

    def check_teached_course(self):
        r = requests.get("http://127.0.0.1:8000/courses")
        data = json.loads(r.text)
        for i in data:
            if i['_Courses__teacher'] == self.__username:
                self.__teached_refcode.append(i['_Courses__refcode'])
                self.__teached_title.append(i['_Courses__title'])

    def modify_course_detail(self, refcode):
        print(refcode)

    def modify_course_material(self, refcode):
        print(refcode)
        EditMaterial(refcode)

    def modify_course_exam(self, refcode):
        print(refcode)
        ExamEditor(refcode)

TeacherDashboard("teach1")