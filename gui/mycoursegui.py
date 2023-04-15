from tkinter import *
from tkinter.font import *
import tkinter.messagebox
import requests
import json

user = "ffwatcharin"

def get_enrolled_course(username):
    global response
    url = "http://localhost:8000/enrolled?username="+str(username)
    r = requests.get(url)
    data = json.loads(r.text)
    if data:
        display = []
        for i in data:
            enrolled_list = i['_Courses__refcode'] + ":" + i['_Courses__title']
            display.append(enrolled_list)
        response = display
    else:
        response = ['No course enrolled!']

def unenroll(username, refcode):
    colonindex = refcode.index(":")
    refcode = refcode[:colonindex]
    print(refcode)
    param = {
        "username": str(username),
        "refcode": str(refcode)
    }
    r = requests.post("http://localhost:8000/unenroll", json=param)
    res = r.text
    print(res)
    tkinter.messagebox.showinfo(title="Success", message="Unenroll Success!")

get_enrolled_course(user)
# --------------------- Create GUI ----------------------- #
mycourse = Tk()
header_font = Font(family="Kanit", weight="bold", size=20)
normal_font = Font(family="Kanit", weight="normal", size=16)
txtbox_font = Font(family="Kanit", weight="normal", size=12)
mycourse.title("My Course")
mycourse.geometry("700x700")
mycourse.resizable(width=False, height=False)

# --- Menu --- #
menuitem = Menu()
menuitem.add_cascade(label='Your Account: ' + str(user))
menuitem.add_cascade(label='About')
menuitem.add_cascade(label='Exit')
mycourse.config(menu=menuitem)

Label(text="My Course", font=header_font).pack(anchor="center")
posy = 50
for i in response:
    lbl = Label(text=i, font=txtbox_font)
    lbl.place(x=50, y=posy)
    Button(text="Study", font=txtbox_font).place(x=500, y=posy)
    Button(text="Unenroll", font=txtbox_font, command=lambda: unenroll(user, lbl.cget("text"))).place(x=570, y=posy)
    posy += 50
mycourse.mainloop()