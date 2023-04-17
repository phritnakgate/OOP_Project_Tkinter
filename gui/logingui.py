from tkinter import *
from tkinter.font import *
import tkinter.messagebox
import requests
import json
from coursecataloggui import CourseCatalog

class LoginGUI:
    def __init__(self):
        self.__login = Tk()
        self.__header_font = Font(family="Kanit", weight="bold", size=20)
        self.__normal_font = Font(family="Kanit", weight="normal", size=16)
        self.__txtbox_font = Font(family="Kanit", weight="normal", size=12)
        self.__login.title("Login")
        self.__login.geometry("300x300")
        self.__login.resizable(width=False, height=False)
        Label(text="Login", font=self.__header_font).pack(anchor="center")
        Label(text="Username:", font=self.__normal_font).place(x=25, y=50)
        self.__username_entry = Entry(self.__login, font=self.__txtbox_font)
        self.__username_entry.place(x=130, y=50)
        Label(text="Password:", font=self.__normal_font).place(x=25, y=80)
        self.__pwd_entry = Entry(self.__login, font=self.__txtbox_font, show="*")
        self.__pwd_entry.place(x=130, y=80)
        Button(text="Login", font=self.__normal_font, command=self.login).place(x=110, y=120)
        self.__login.mainloop()
    def login(self):
        if self.__username_entry.get() != "" and self.__pwd_entry.get() != "":
            url = "http://localhost:8000/login?username="+str(self.__username_entry.get())+"&password="+str(self.__pwd_entry.get())
            print(url)
            r = requests.post(url)
            data = json.loads(r.text)
            print(data)
            if data == {'Status': 'Username/Password Incorrect!!'}:
                tkinter.messagebox.showerror(title="Error", message="Username/Password is Incorrect!!")
            else:
                tkinter.messagebox.showinfo(title="Success", message="Welcome "+data['username'])
                self.__login.destroy()
                CourseCatalog(data['username'])
        else:
            tkinter.messagebox.showerror(title="Error", message="Username/Password is blank!")
#LoginGUI()