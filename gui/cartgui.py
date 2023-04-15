from tkinter import *
from tkinter.font import *
import tkinter.messagebox
import requests
import json
from random import randint

user = "ffwatcharin"


def update_cart():
    r = requests.get("http://localhost:8000/cart")
    data = json.loads(r.text)
    cart_item = data["Cart"]
    if cart_item:
        display = []
        for i in cart_item:
            cart_list = i['_Courses__refcode'] + ":" + i['_Courses__title']
            display.append(cart_list)
        return display
    else:
        return ['No course in cart']


response = update_cart()
print(response)


def enroll():
    url = "http://localhost:8000/enroll?user=" + str(user)
    if response != ['No course in cart']:
        requests.post(url)
        tkinter.messagebox.showinfo(title="Success", message="Enroll Success!")
        cartui.destroy()
    else:
        tkinter.messagebox.showerror(title="Error", message="Cart is Empty!")


def refresh():
    response = update_cart()
    print(response)


cartui = Tk()

header_font = Font(family="Kanit", weight="bold", size=20)
normal_font = Font(family="Kanit", weight="normal", size=16)
txtbox_font = Font(family="Kanit", weight="normal", size=12)
cartui.title("Cart")
cartui.geometry("500x500")
cartui.resizable(width=False, height=False)

menuitem = Menu()
menuitem.add_cascade(label='Your Account: ' + str(user))
menuitem.add_cascade(label='About')
menuitem.add_cascade(label='Exit')
cartui.config(menu=menuitem)

Label(text="Cart", font=header_font).pack(anchor="center")
Button(text="Refresh Cart", font=normal_font, command=refresh).pack(anchor="e")
lbl = Label(cartui, font=normal_font)
lbl.pack(anchor="center")


def update():
    for i in response:
        lbl['text'] = i + "\n"
    cartui.after(1000, update)  # run itself again after 1000 ms


Button(text="Enroll", font=normal_font, command=enroll).pack(anchor="center")

update()
cartui.mainloop()
