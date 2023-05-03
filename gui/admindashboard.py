from tkinter import ttk, StringVar
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring

import customtkinter as ctk
import requests
import json
from functools import partial

from customtkinter import CTkToplevel
from tkcalendar import DateEntry
from tkinter import messagebox

from gui.editprofile import EditProfile
from gui.editexamgui import ExamEditor
from gui.editmaterial import EditMaterial

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class AdminDashboard:
    def __init__(self):
        self.__user_db = []
        self.__course_db = []

        self.__adash = ctk.CTk()
        self.__header_font = ctk.CTkFont(family="Kanit", weight="bold", size=20)
        self.__normal_font = ctk.CTkFont(family="Kanit", weight="normal", size=16)
        self.__txtbox_font = ctk.CTkFont(family="Kanit", weight="normal", size=12)
        self.__adash.title("Admin Dashboard")
        self.__adash.geometry("500x500")
        self.__adash.resizable(width=False, height=False)
        self.screen(500, 500)
        ctk.CTkLabel(self.__adash, text="Admin Dashboard", font=self.__header_font).grid(row=0, column=1)
        ctk.CTkLabel(self.__adash, text="=" * 20, font=self.__header_font).grid(row=1, column=1)

        ctk.CTkLabel(self.__adash, text="User Zone", font=self.__header_font).grid(row=2, column=0)
        ctk.CTkButton(self.__adash, text="Create User", font=self.__txtbox_font, command=self.create_user).grid(row=3,column=0)
        ctk.CTkButton(self.__adash, text="Modify User", font=self.__txtbox_font, command=self.modify_u).grid(row=3, column=1)
        ctk.CTkButton(self.__adash, text="Delete User", font=self.__txtbox_font, command=self.delete_u).grid(row=3, column=2)
        ctk.CTkLabel(self.__adash, text="User data", font=self.__normal_font).grid(row=4, column=0)
        self.__usertxt = ctk.CTkTextbox(self.__adash, font=self.__txtbox_font, height=100, width=200)
        self.__usertxt.grid(row=5, column=1)
        self.get_user_data()

        ctk.CTkLabel(self.__adash, text="=" * 20, font=self.__header_font).grid(row=6, column=1)

        ctk.CTkLabel(self.__adash, text="Course Zone", font=self.__header_font).grid(row=7, column=0)
        ctk.CTkButton(self.__adash, text="Create Course", font=self.__txtbox_font).grid(row=8, column=0)
        ctk.CTkButton(self.__adash, text="Modify Course", font=self.__txtbox_font, command=self.modify_c).grid(row=8, column=1)
        ctk.CTkButton(self.__adash, text="Delete Course", font=self.__txtbox_font, command=self.delete_c).grid(row=8, column=2)
        ctk.CTkLabel(self.__adash, text="Course data", font=self.__normal_font).grid(row=9, column=0)
        self.__ctxt = ctk.CTkTextbox(self.__adash, font=self.__txtbox_font, height=100, width=200)
        self.__ctxt.grid(row=10, column=1)
        self.get_course_data()

        self.__adash.mainloop()

    def screen(self, width, height):
        self.screen_width = self.__adash.winfo_screenwidth()
        self.screen_height = self.__adash.winfo_screenheight()
        self.x = (self.screen_width // 2) - (width // 2)
        self.y = (self.screen_height // 2) - (height // 2)
        self.__adash.geometry(f"{width}x{height}+{self.x}+{self.y}")

    def create_user(self):
        RegisterGUI()

    def get_user_data(self):
        r = requests.get("http://localhost:8000/all_users")
        self.__user_db = []
        for i in json.loads(r.text):
            self.__user_db.append(i['_User__user_type'] + ": " + i['_User__username'])
        self.__usertxt.delete("0.0", "end-1c")
        for j in self.__user_db:
            self.__usertxt.insert("end", j + "\n")

    def get_course_data(self):
        r = requests.get("http://localhost:8000/courses")
        self.__course_db = []
        for i in json.loads(r.text):
            self.__course_db.append(i['_Courses__refcode'] + ": " + i['_Courses__title'])
        self.__ctxt.delete("0.0", "end-1c")
        for j in self.__course_db:
            self.__ctxt.insert("end", j + "\n")

    def modify_u(self):
        ask_user = askstring('User Modification', 'Enter Username')
        ask_ust = askstring('User Modification', 'Enter UserType')
        EditProfile(ask_user, ask_ust)
    def delete_u(self):
        ask_user = askstring('User Deletion', 'Enter Username')
        url = "http://localhost:8000/delete_user?username="+str(ask_user)
        r = requests.delete(url)
        if json.loads(r.text) == {"message": "Username has been deleted"}:
            self.get_user_data()
            showinfo(title="Success", message="Delete Success!")
    def delete_c(self):
        ask_c = askstring('Course Deletion', 'Enter Refcode')
        url = "http://localhost:8000/delete_course?refcode="+ask_c
        requests.delete(url)
        self.get_course_data()
    def modify_c(self):
        ModifyCourse()

class RegisterGUI:
    def __init__(self):
        self.__txtcolor = "white"
        self.__bgcolor = "#242424"
        self.__entrycolor = "gray20"

        self.__register = CTkToplevel()
        self.__header_font = ctk.CTkFont(family="Kanit", weight="bold", size=20)
        self.__normal_font = ctk.CTkFont(family="Kanit", weight="normal", size=16)
        self.__txtbox_font = ctk.CTkFont(family="Kanit", weight="normal", size=12)
        self.__register.title("Create User")
        self.__register.geometry("400x500")
        self.__register.config(bg=self.__bgcolor)
        self.__register.resizable(width=False, height=False)

        ctk.CTkLabel(self.__register, text="Create User", font=self.__header_font).pack()

        ctk.CTkLabel(self.__register, text="Username :", font=self.__normal_font).place(x=25, y=50)
        self.__username_entry = ctk.CTkEntry(self.__register, font=self.__txtbox_font)
        self.__username_entry.place(x=140, y=55)

        ctk.CTkLabel(self.__register, text="Password :", font=self.__normal_font).place(x=25, y=80)
        self.__pwd_entry = ctk.CTkEntry(self.__register, font=self.__txtbox_font, show="*")
        self.__pwd_entry.place(x=140, y=85)

        ctk.CTkLabel(self.__register, text="Email :", font=self.__normal_font).place(x=25, y=110)
        self.__email_entry = ctk.CTkEntry(self.__register, font=self.__txtbox_font)
        self.__email_entry.place(x=140, y=115)

        ctk.CTkLabel(self.__register, text="Name :", font=self.__normal_font).place(x=25, y=140)
        self.__name_entry = ctk.CTkEntry(self.__register, font=self.__txtbox_font)
        self.__name_entry.place(x=140, y=145)

        ctk.CTkLabel(self.__register, text="Surname :", font=self.__normal_font).place(x=25, y=170)
        self.__surname_entry = ctk.CTkEntry(self.__register, font=self.__txtbox_font)
        self.__surname_entry.place(x=140, y=175)

        ctk.CTkLabel(self.__register, text="Gender :", font=self.__normal_font).place(x=25, y=200)
        n = StringVar()
        self.__genderChoose = ttk.Combobox(self.__register, width=10, textvariable=n)
        self.__genderChoose['values'] = ('Male', 'Female', 'Other')
        self.__genderChoose.place(x=140, y=210)
        self.__genderChoose.current()

        ctk.CTkLabel(self.__register, text="BirthDate :", font=self.__normal_font).place(x=25, y=230)
        self.__cal = DateEntry(self.__register, width=10,
                               background="blue", foreground="skyblue", bd=4)
        self.__cal.place(x=140, y=240)

        ctk.CTkLabel(self.__register, text="Education :", font=self.__normal_font).place(x=25, y=260)
        self.__educate_entry = ctk.CTkEntry(self.__register, font=self.__txtbox_font)
        self.__educate_entry.place(x=140, y=265)

        ctk.CTkLabel(self.__register, text="Province :", font=self.__normal_font).place(x=25, y=290)
        self.__prov_entry = ctk.CTkEntry(self.__register, font=self.__txtbox_font)
        self.__prov_entry.place(x=140, y=295)

        ctk.CTkLabel(self.__register, text="Country :", font=self.__normal_font).place(x=25, y=320)
        self.__country_entry = ctk.CTkEntry(self.__register, font=self.__txtbox_font)
        self.__country_entry.place(x=140, y=325)

        ctk.CTkLabel(self.__register, text="UserType :", font=self.__normal_font).place(x=25, y=350)
        i = StringVar()
        self.__userTypeChoose = ttk.Combobox(
            self.__register, width=10, textvariable=i)
        self.__userTypeChoose['values'] = ('Teacher', 'Student')
        self.__userTypeChoose.place(x=140, y=360)
        self.__userTypeChoose.current()

        ctk.CTkButton(self.__register, text="register", font=self.__normal_font, command=self.register).place(x=140,
                                                                                                              y=390)
        self.__register.mainloop()

    def register(self):
        if self.__username_entry.get() == "" or self.__pwd_entry.get() == "" or (
                self.__userTypeChoose.get() not in ['Teacher', 'Student']):
            messagebox.showerror(message="Please enter a Username, Password and UserType", title="Error")
        else:
            data = {
                "username": self.__username_entry.get(),
                "password": self.__pwd_entry.get(),
                "email": self.__email_entry.get(),
                "fname": self.__name_entry.get(),
                "lname": self.__surname_entry.get(),
                "gender": self.__genderChoose.get(),
                "birth_date": self.__cal.get(),
                "education": self.__educate_entry.get(),
                "province": self.__pwd_entry.get(),
                "country": self.__country_entry.get(),
                "user_type": self.__userTypeChoose.get()
            }
            if self.__userTypeChoose.get() == 'Teacher':
                self.__show_dept = askstring('Department', 'Enter your Department?')
                showinfo('Your Department', 'Your Department is {}'.format(self.__show_dept))
                if self.__show_dept is not None:  # user pressed OK
                    # print(self.__show_dept)
                    data['teacher_dept'] = self.__show_dept
                else:  # user pressed Cancel
                    print("User cancelled")
                    data['teacher_dept'] = ""
            r = requests.post("http://127.0.0.1:8000/register", json=data)
            res = json.loads(r.text)
            # print(data)
            # print(res)
            messagebox.showinfo(message="Create Success!", title="Success!")
            self.__register.destroy()

class ModifyCourse:
    def __init__(self):
        self.__refcode = []
        self.__title = []
        self.__posy = 100
        self.__tdash = ctk.CTkToplevel()
        self.__header_font = ctk.CTkFont(family="Kanit", weight="bold", size=20)
        self.__normal_font = ctk.CTkFont(family="Kanit", weight="normal", size=16)
        self.__txtbox_font = ctk.CTkFont(family="Kanit", weight="normal", size=12)
        self.__tdash.title("Modify Course")
        self.__tdash.geometry("900x900")
        ctk.CTkLabel(self.__tdash, text="Modify Course", font=self.__header_font).pack()

        self.check_teached_course()
        for i in range(len(self.__refcode)):
            ctk.CTkLabel(self.__tdash, text=self.__refcode[i]+":"+self.__title[i], font=self.__normal_font).place(x=50, y=self.__posy)
            ctk.CTkButton(self.__tdash, text="Modify Detail", font=self.__txtbox_font,
                          command=partial(self.modify_course_detail, self.__refcode[i])).place(x=400, y=self.__posy)
            ctk.CTkButton(self.__tdash, text="Modify Material", font=self.__txtbox_font,
                          command=partial(self.modify_course_material, self.__refcode[i])).place(x=550, y=self.__posy)
            ctk.CTkButton(self.__tdash, text="Modify Exam", font=self.__txtbox_font,
                          command=partial(self.modify_course_exam, self.__refcode[i])).place(x=700, y=self.__posy)
            self.__posy += 50
        self.__tdash.mainloop()

    def check_teached_course(self):
        r = requests.get("http://127.0.0.1:8000/courses")
        data = json.loads(r.text)
        for i in data:
            self.__refcode.append(i['_Courses__refcode'])
            self.__title.append(i['_Courses__title'])

    def modify_course_detail(self, refcode):
        pass
        # print(refcode)

    def modify_course_material(self, refcode):
        # print(refcode)
        EditMaterial(refcode)

    def modify_course_exam(self, refcode):
        # print(refcode)
        ExamEditor(refcode)
#AdminDashboard()
