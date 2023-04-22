from tkinter import *
from tkinter.font import *
import tkinter.messagebox
import requests
import json
from gui.studygui import Study
from functools import partial


class MyCourseGUI:
    def __init__(self, username):
        self.__user = username
        self.__response = None
        # --------------------- Create GUI ----------------------- #
        self.__mycourse = Tk()
        self.__header_font = Font(family="Kanit", weight="bold", size=20)
        self.__normal_font = Font(family="Kanit", weight="normal", size=16)
        self.__txtbox_font = Font(family="Kanit", weight="normal", size=12)
        self.__mycourse.title("My Course")
        self.__mycourse.geometry("700x700")
        self.__mycourse.resizable(width=False, height=False)
        
        # --- Menu --- #
        self.__menuitem = Menu()
        self.__menuitem.add_cascade(label='Your Account: ' + str(self.__user))
        self.__menuitem.add_cascade(label='About')
        self.__menuitem.add_cascade(label='Exit')
        self.__mycourse.config(menu=self.__menuitem)
        
        Label(text="My Course", font=self.__header_font).pack(anchor="center")
        posy = 50
        self.get_enrolled_course()
        if self.__response == ['No course enrolled!']:
            Label(text='No course enrolled!', font=self.__txtbox_font)
        else:
            for i in self.__response:
                lbl = Label(text=i, font=self.__txtbox_font)
                lbl.place(x=50, y=posy)
                Button(text="Study", font=self.__txtbox_font, command=partial(self.study, lbl.cget("text"))).place(x=500, y=posy)
                Button(text="Unenroll", font=self.__txtbox_font, command=partial(self.unenroll, lbl.cget("text"))).place(x=570, y=posy)
                posy += 50
        self.__mycourse.mainloop()

    def get_enrolled_course(self):
        url = "http://localhost:8000/enrolled?username=" + str(self.__user)
        r = requests.get(url)
        data = json.loads(r.text)
        if data:
            display = []
            for i in data:
                enrolled_list = i['_Courses__refcode'] + ":" + i['_Courses__title']
                display.append(enrolled_list)
            self.__response = display
        else:
            self.__response = ['No course enrolled!']

    def unenroll(self, refcode):
        colonindex = refcode.index(":")
        refcode = refcode[:colonindex]
        print(refcode)
        param = {
            "username": str(self.__user),
            "refcode": str(refcode)
        }
        r = requests.post("http://localhost:8000/unenroll", json=param)
        res = r.text
        print(res)
        tkinter.messagebox.showinfo(title="Success", message="Unenroll Success! Please reopen this window")

    def study(self, refcode):
        colonindex = refcode.index(":")
        refcode = refcode[:colonindex]
        self.__mycourse.destroy()
        Study(self.__user, refcode)
        
# MyCourseGUI("ffwatcharin")
