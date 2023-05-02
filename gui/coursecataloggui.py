from tkinter import *
from tkinter.font import *
import tkinter.messagebox
from tkinter.messagebox import showinfo
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter.simpledialog import askstring
import requests
import json
import customtkinter
from functools import partial

from gui.mycoursegui import MyCourseGUI
from gui.coursedetailgui import CourseDetail
from gui.cartgui import CartGUI
from gui.browsebycatg import BrowseCatg
from gui.teacherdashboard import TeacherDashboard
from gui.admindashboard import AdminDashboard
from gui.editprofile import EditProfile

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

# ------------------ CourseCatalog ------------------ #
class CourseCatalog:
    def __init__(self, username, user_type):
        self.__username = username
        self.__user_type = user_type
        self.__all_course = []
        self.__total_course = 0
        self.__row_base = 4
        self.__txtcolor = "white"
        self.__bgcolor = "#242424"
        # ------ Create GUI ------ #
        self.__catalog = Tk()
        self.__header_font = Font(family="Kanit", weight="bold", size=20)
        self.__normal_font = Font(family="Kanit", weight="normal", size=16)
        self.__txtbox_font = Font(family="Kanit", weight="normal", size=12)
        self.__catalog.title("CE MOOC")
        self.screen(1100,1000)
        self.__catalog.config(bg=self.__bgcolor)
        # self.__catalog.resizable(width=False, height=False)
        # Menu #
        self.__guestaccountmenu = Menu()
        self.__guestaccountmenu.add_command(label="Register", command=self.register_gui)
        self.__guestaccountmenu.add_command(label="Login", command=self.login_gui)

        self.__studentaccountmenu = Menu()
        self.__studentaccountmenu.add_command(label="My Courses", command=self.my_course)
        self.__studentaccountmenu.add_command(label="My Cart", command=self.cart)
        self.__studentaccountmenu.add_command(label="Edit Profile", command=self.edit_profile)
        self.__studentaccountmenu.add_command(label="Logout & Close Program", command=self.logout)

        self.__teacheraccountmenu = Menu()
        self.__teacheraccountmenu.add_command(label="My Teached Courses", command=self.tdashboard)
        self.__teacheraccountmenu.add_command(label="Edit Profile")
        self.__teacheraccountmenu.add_command(label="Logout & Close Program", command=self.logout)

        self.__adminaccountmenu = Menu()
        self.__adminaccountmenu.add_command(label="Admin Portal", command=self.adashboard)
        self.__adminaccountmenu.add_command(label="Logout & Close Program", command=self.logout)

        self.__menuitem = Menu()
        if self.__username == "Guest":
            self.__menuitem.add_cascade(label='Your Account: ' + str(self.__username), menu=self.__guestaccountmenu)
        else:
            if self.__user_type == "Student":
                self.__menuitem.add_cascade(label='Your Account: ' + str(self.__username),
                                            menu=self.__studentaccountmenu)
            elif self.__user_type == "Teacher":
                self.__menuitem.add_cascade(label='Your Account: ' + str(self.__username),menu=self.__teacheraccountmenu)
            elif self.__user_type == "Admin":
                self.__menuitem.add_cascade(label='Your Account: ' + str(self.__username), menu=self.__adminaccountmenu)
        self.__menuitem.add_cascade(label='About', command=self.aboutbox)
        self.__menuitem.add_cascade(label='Exit', command=self.logout)
        self.__catalog.config(menu=self.__menuitem)

        # Catalog Header #
        Label(text="Welcome To CE MOOC", font=self.__header_font, fg=self.__txtcolor, bg=self.__bgcolor).grid(row=0, column=1)
        if self.__username == "Guest":
            self.__row_base = 5
            Label(text="Please Login to Enroll!", font=self.__normal_font, fg="red", bg=self.__bgcolor).grid(row=1, column=1)
            
            Label(text="========== Category ==========", font=self.__header_font, fg=self.__txtcolor, bg=self.__bgcolor).grid(row=2,column=1)
            # Label(text="==========", font=self.__normal_font, fg=self.__txtcolor, bg=self.__bgcolor).grid(row=2, column=1)
            Button(text='Software', font=self.__txtbox_font,
                   fg=self.__txtcolor, bg="#1F6AA5", activebackground=self.__bgcolor,
                   activeforeground=self.__txtcolor, command=partial(self.browse_catg,'Software')).grid(
                row=3, column=0)
            Button(text='Hardware', font=self.__txtbox_font,
                   fg=self.__txtcolor, bg="#1F6AA5", activebackground=self.__bgcolor,
                   activeforeground=self.__txtcolor, command=partial(self.browse_catg,'Hardware')).grid(
                row=3, column=1)
            Button(text='Math', font=self.__txtbox_font,
                   fg=self.__txtcolor, bg="#1F6AA5", activebackground=self.__bgcolor,
                   activeforeground=self.__txtcolor, command=partial(self.browse_catg,'Math')).grid(
                row=3, column=2)
            Button(text='Science', font=self.__txtbox_font,
                   fg=self.__txtcolor, bg="#1F6AA5", activebackground=self.__bgcolor,
                   activeforeground=self.__txtcolor, command=partial(self.browse_catg,'Science')).grid(
                row=3, column=3)
            Button(text='English', font=self.__txtbox_font,
                   fg=self.__txtcolor, bg="#1F6AA5", activebackground=self.__bgcolor,
                   activeforeground=self.__txtcolor, command=partial(self.browse_catg,'English')).grid(
                row=3, column=4)
            Label(text="==============================", font=self.__header_font, fg=self.__txtcolor, bg=self.__bgcolor).grid(row=4,column=1)
        else:
            Label(text="========== Category ==========", font=self.__header_font, fg=self.__txtcolor, bg=self.__bgcolor).grid(row=1,column=1)
            # Label(text="==========", font=self.__normal_font, fg=self.__txtcolor, bg=self.__bgcolor).grid(row=1, column=1)
            Button(text='Software', font=self.__txtbox_font,
                   fg=self.__txtcolor, bg="#1F6AA5", activebackground=self.__bgcolor,
                   activeforeground=self.__txtcolor,command=partial(self.browse_catg,'Software')).grid(
                row=2, column=0)
            Button(text='Hardware', font=self.__txtbox_font,
                   fg=self.__txtcolor, bg="#1F6AA5", activebackground=self.__bgcolor,
                   activeforeground=self.__txtcolor, command=partial(self.browse_catg,'Hardware')).grid(
                row=2, column=1)
            Button(text='Math', font=self.__txtbox_font,
                   fg=self.__txtcolor, bg="#1F6AA5", activebackground=self.__bgcolor,
                   activeforeground=self.__txtcolor, command=partial(self.browse_catg,'Math')).grid(
                row=2, column=2)
            Button(text='Science', font=self.__txtbox_font,
                   fg=self.__txtcolor, bg="#1F6AA5", activebackground=self.__bgcolor,
                   activeforeground=self.__txtcolor, command=partial(self.browse_catg,'Science')).grid(
                row=2, column=3)
            Button(text='English', font=self.__txtbox_font,
                   fg=self.__txtcolor, bg="#1F6AA5", activebackground=self.__bgcolor,
                   activeforeground=self.__txtcolor, command=partial(self.browse_catg,'English')).grid(
                row=2, column=4)
            Label(text="==============================", font=self.__header_font, fg=self.__txtcolor, bg=self.__bgcolor).grid(row=3, column=1)

        # All Courses #
        self.get_all_course()
        if self.__total_course % 3 == 1:
            for i in range(0, self.__total_course - 3, 3):
                for j in range(3):
                    Label(text=self.__all_course[i + j]['_Courses__refcode'], font=self.__normal_font, fg=self.__txtcolor, bg=self.__bgcolor).grid(
                        row=self.__row_base, column=j)
                    Label(text=self.__all_course[i + j]['_Courses__title'], font=self.__normal_font, fg=self.__txtcolor, bg=self.__bgcolor).grid(
                        row=self.__row_base + 1, column=j)
                    Button(text='Detail', font=self.__txtbox_font,
                           command=partial(self.detail, str(self.__all_course[i + j]['_Courses__refcode'])),
                           fg=self.__txtcolor, bg="#1F6AA5", activebackground=self.__bgcolor,
                           activeforeground=self.__txtcolor).grid(
                        row=self.__row_base + 2, column=j)
                self.__row_base += 3
            Label(text=self.__all_course[i + j + 1]['_Courses__refcode'], font=self.__normal_font, fg=self.__txtcolor, bg=self.__bgcolor).grid(
                row=self.__row_base, column=0)
            Label(text=self.__all_course[i + j + 1]['_Courses__title'], font=self.__normal_font, fg=self.__txtcolor, bg=self.__bgcolor).grid(
                row=self.__row_base + 1, column=0)
            Button(text='Detail', font=self.__txtbox_font,
                   command=partial(self.detail, str(self.__all_course[i + j]['_Courses__refcode'])), fg=self.__txtcolor,
                   bg="#1F6AA5", activebackground=self.__bgcolor, activeforeground=self.__txtcolor).grid(
                row=self.__row_base + 2, column=0)
        elif self.__total_course % 3 == 2:
            for i in range(0, self.__total_course - 3, 3):
                for j in range(3):
                    Label(text=self.__all_course[i + j]['_Courses__refcode'], font=self.__normal_font, fg=self.__txtcolor, bg=self.__bgcolor).grid(
                        row=self.__row_base, column=j)
                    Label(text=self.__all_course[i + j]['_Courses__title'], font=self.__normal_font, fg=self.__txtcolor, bg=self.__bgcolor).grid(
                        row=self.__row_base + 1, column=j)
                    Button(text='Detail', font=self.__txtbox_font,
                           command=partial(self.detail, str(self.__all_course[i + j]['_Courses__refcode'])),
                           fg=self.__txtcolor, bg="#1F6AA5", activebackground=self.__bgcolor,
                           activeforeground=self.__txtcolor).grid(
                        row=self.__row_base + 2, column=j)
                self.__row_base += 3
            for k in range(2):
                Label(text=self.__all_course[i + j + k + 1]['_Courses__refcode'], font=self.__normal_font, fg=self.__txtcolor, bg=self.__bgcolor).grid(
                    row=self.__row_base, column=k)
                Label(text=self.__all_course[i + j + k + 1]['_Courses__title'], font=self.__normal_font, fg=self.__txtcolor, bg=self.__bgcolor).grid(
                    row=self.__row_base + 1, column=k)
                Button(text='Detail', font=self.__txtbox_font,
                       command=partial(self.detail, str(self.__all_course[i + j]['_Courses__refcode'])),
                       fg=self.__txtcolor, bg="#1F6AA5", activebackground=self.__bgcolor,
                       activeforeground=self.__txtcolor).grid(
                    row=self.__row_base + 2, column=k)
        elif self.__total_course % 3 == 0:
            for i in range(0, self.__total_course, 3):
                for j in range(3):
                    Label(text=self.__all_course[i + j]['_Courses__refcode'], font=self.__normal_font, fg=self.__txtcolor, bg=self.__bgcolor).grid(
                        row=self.__row_base, column=j)
                    Label(text=self.__all_course[i + j]['_Courses__title'], font=self.__normal_font, fg=self.__txtcolor, bg=self.__bgcolor).grid(
                        row=self.__row_base + 1, column=j)
                    Button(text='Detail', font=self.__txtbox_font,
                           command=partial(self.detail, str(self.__all_course[i + j]['_Courses__refcode'])), fg=self.__txtcolor, bg="#1F6AA5", activebackground=self.__bgcolor, activeforeground=self.__txtcolor).grid(
                        row=self.__row_base + 2, column=j)
                self.__row_base += 3
        # print(self.__row_base)

        # Course Recommendation #
        Label(text="========== Recommended ==========", font=self.__header_font, fg=self.__txtcolor, bg=self.__bgcolor).grid(row=self.__row_base, column=1)

        self.__catalog.mainloop()
        
    def screen(self, width, height):
        self.screen_width = self.__catalog.winfo_screenwidth()
        self.screen_height = self.__catalog.winfo_screenheight()             
        self.x = (self.screen_width // 2) - (width // 2)
        self.y = (self.screen_height // 2) - (height // 2)
        self.__catalog.geometry(f"{width}x{height}+{self.x}+{self.y}")

    def get_all_course(self):
        r = requests.get("http://localhost:8000/courses")
        data = json.loads(r.text)
        self.__total_course = len(data)
        for i in data:
            self.__all_course.append(i)

    def register_gui(self):
        self.__catalog.destroy()
        RegisterGUI()

    def login_gui(self):
        self.__catalog.destroy()
        LoginGUI()

    def logout(self):
        answer = tkinter.messagebox.askyesno(title='Confirmation', message='Are you sure that you want to quit?')
        if answer:
            self.__catalog.destroy()

    def my_course(self):
        #self.__catalog.destroy()
        MyCourseGUI(self.__username)

    def detail(self, ref):
        CourseDetail(self.__username, ref, self.__user_type)

    def cart(self):
        CartGUI(self.__username)
    
    def browse_catg(self, category):
        BrowseCatg(category, self.__username, self.__user_type)

    def aboutbox(self):
        tkinter.messagebox.showinfo(title="About", message="CE MOOC By.. Phrit, Watcharin, Yongsuk and Paramate")

    def tdashboard(self):
        self.__catalog.destroy()
        TeacherDashboard(self.__username)

    def adashboard(self):
        self.__catalog.destroy()
        AdminDashboard()

    def edit_profile(self):
        EditProfile(self.__username, self.__user_type)

# ------------------ Login ------------------ #
class LoginGUI:
    def __init__(self):
        self.__login = customtkinter.CTk()
        self.__header_font = customtkinter.CTkFont(family="Kanit", weight="bold", size=20)
        self.__normal_font = customtkinter.CTkFont(family="Kanit", weight="normal", size=16)
        self.__txtbox_font = customtkinter.CTkFont(family="Kanit", weight="normal", size=12)
        self.__login.title("Login")
        self.__login.geometry("300x300")
        self.__login.resizable(width=False, height=False)
        customtkinter.CTkLabel(self.__login, text="Login", font=self.__header_font).pack(anchor="center")
        customtkinter.CTkLabel(self.__login, text="Username:", font=self.__normal_font).place(x=25, y=50)
        self.__username_entry = customtkinter.CTkEntry(self.__login, font=self.__txtbox_font)
        self.__username_entry.place(x=130, y=50)
        customtkinter.CTkLabel(self.__login, text="Password:", font=self.__normal_font).place(x=25, y=80)
        self.__pwd_entry = customtkinter.CTkEntry(self.__login, font=self.__txtbox_font, show="*")
        self.__pwd_entry.place(x=130, y=80)
        customtkinter.CTkButton(self.__login, text="Login", font=self.__normal_font, command=self.login).place(x=110, y=120)
        self.__login.mainloop()

    def login(self):
        if self.__username_entry.get() != "" and self.__pwd_entry.get() != "":
            url = "http://localhost:8000/login?username=" + str(self.__username_entry.get()) + "&password=" + str(
                self.__pwd_entry.get())
            print(url)
            r = requests.post(url)
            data = json.loads(r.text)
            # print(data)
            if data == {'Status': 'Username/Password Incorrect!!'}:
                tkinter.messagebox.showerror(title="Error", message="Username/Password is Incorrect!!")
            else:
                tkinter.messagebox.showinfo(title="Success", message="Welcome " + data['username'])
                self.__login.destroy()
                CourseCatalog(data['username'], data['user_type'])
        else:
            tkinter.messagebox.showerror(title="Error", message="Username/Password is blank!")


# ------------------ Register ------------------ #
class RegisterGUI:
    def __init__(self):
        self.__txtcolor = "white"
        self.__bgcolor = "#242424"
        self.__entrycolor = "gray20"

        self.__register = Tk()
        self.__header_font = Font(family="Kanit", weight="bold", size=20)
        self.__normal_font = Font(family="Kanit", weight="normal", size=16)
        self.__txtbox_font = Font(family="Kanit", weight="normal", size=12)
        self.__register.title("Register")
        self.__register.geometry("400x500")
        self.__register.config(bg=self.__bgcolor)
        self.__register.resizable(width=False, height=False)

        Label(text="Register", font=self.__header_font, fg=self.__txtcolor, bg=self.__bgcolor).pack()

        Label(text="Username :", font=self.__normal_font, fg=self.__txtcolor, bg=self.__bgcolor).place(x=25, y=50)
        self.__username_entry = Entry(self.__register, font=self.__txtbox_font, fg=self.__txtcolor, bg=self.__entrycolor)
        self.__username_entry.place(x=140, y=55)

        Label(text="Password :", font=self.__normal_font, fg=self.__txtcolor, bg=self.__bgcolor).place(x=25, y=80)
        self.__pwd_entry = Entry(self.__register, font=self.__txtbox_font, show="*", fg=self.__txtcolor, bg=self.__entrycolor)
        self.__pwd_entry.place(x=140, y=85)

        Label(text="Email :", font=self.__normal_font, fg=self.__txtcolor, bg=self.__bgcolor).place(x=25, y=110)
        self.__email_entry = Entry(self.__register, font=self.__txtbox_font, fg=self.__txtcolor, bg=self.__entrycolor)
        self.__email_entry.place(x=140, y=115)

        Label(text="Name :", font=self.__normal_font, fg=self.__txtcolor, bg=self.__bgcolor).place(x=25, y=140)
        self.__name_entry = Entry(self.__register, font=self.__txtbox_font, fg=self.__txtcolor, bg=self.__entrycolor)
        self.__name_entry.place(x=140, y=145)

        Label(text="Surname :", font=self.__normal_font, fg=self.__txtcolor, bg=self.__bgcolor).place(x=25, y=170)
        self.__surname_entry = Entry(self.__register, font=self.__txtbox_font, fg=self.__txtcolor, bg=self.__entrycolor)
        self.__surname_entry.place(x=140, y=175)

        Label(text="Gender :", font=self.__normal_font, fg=self.__txtcolor, bg=self.__bgcolor).place(x=25, y=200)
        n = StringVar()
        self.__genderChoose = ttk.Combobox(self.__register, width=10, textvariable=n)
        self.__genderChoose['values'] = ('Male', 'Female', 'Other')
        self.__genderChoose.place(x=140, y=210)
        self.__genderChoose.current()

        Label(text="BirthDate :", font=self.__normal_font, fg=self.__txtcolor, bg=self.__bgcolor).place(x=25, y=230)
        self.__cal = DateEntry(self.__register, width=10,
                               background="blue", foreground="skyblue", bd=4)
        self.__cal.place(x=140, y=240)

        Label(text="Education :", font=self.__normal_font, fg=self.__txtcolor, bg=self.__bgcolor).place(x=25, y=260)
        self.__educate_entry = Entry(self.__register, font=self.__txtbox_font, fg=self.__txtcolor, bg=self.__entrycolor)
        self.__educate_entry.place(x=140, y=265)

        Label(text="Province :", font=self.__normal_font, fg=self.__txtcolor, bg=self.__bgcolor).place(x=25, y=290)
        self.__prov_entry = Entry(self.__register, font=self.__txtbox_font, fg=self.__txtcolor, bg=self.__entrycolor)
        self.__prov_entry.place(x=140, y=295)

        Label(text="Country :", font=self.__normal_font, fg=self.__txtcolor, bg=self.__bgcolor).place(x=25, y=320)
        self.__country_entry = Entry(self.__register, font=self.__txtbox_font, fg=self.__txtcolor, bg=self.__entrycolor)
        self.__country_entry.place(x=140, y=325)

        Label(text="UserType :", font=self.__normal_font, fg=self.__txtcolor, bg=self.__bgcolor).place(x=25, y=350)
        i = StringVar()
        self.__userTypeChoose = ttk.Combobox(
            self.__register, width=10, textvariable=i)
        self.__userTypeChoose['values'] = ('Teacher', 'Student')
        self.__userTypeChoose.place(x=140, y=360)
        self.__userTypeChoose.current()

        Button(text="register", font=self.__normal_font, command=self.register, fg=self.__txtcolor, bg="#1F6AA5", activebackground=self.__bgcolor, activeforeground=self.__txtcolor).place(x=140, y=390)
        self.__register.mainloop()

    def register(self):
        if self.__username_entry.get() == "" or self.__pwd_entry.get() == "" or (
                self.__userTypeChoose.get() not in ['Teacher', 'Student']):
            tkinter.messagebox.showerror(message="Please enter a Username, Password and UserType", title="Error")
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
            tkinter.messagebox.showinfo(message="Register Success! Please Login!", title="Success!")
            self.__register.destroy()
            LoginGUI()
