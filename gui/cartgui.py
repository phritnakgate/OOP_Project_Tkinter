from tkinter import *
from tkinter.font import *
import tkinter.messagebox
import requests
import json

user = "ffwatcharin"

def update_cart():
    global response
    r = requests.get("http://localhost:8000/cart")
    data = json.loads(r.text)
    cart_item = data["Cart"]
    if cart_item:
        display = []
        for i in cart_item:
            cart_list = i['_Courses__refcode'] + ":" + i['_Courses__title']
            display.append(cart_list)
        response = display
    else:
        response = ['No course in cart']

update_cart()
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
    update_cart()
    print(response)
    txtbox.config(state="normal")
    txtbox.delete("1.0", "end-1c")
    for j in response:
        txtbox.insert(END, j + "\n")
    txtbox.config(state="disabled")
def remove_cart():
    ref = ent.get()
    print(ref)
    if ref != "" and response != ['No course in cart']:
        req = {"refcode": str(ref)}
        r = requests.post("http://localhost:8000/removecart", json=req)
        res = r.text
        print(res)
        if res == "{\"Success\":\"Remove complete\"}":
            ent.delete(0, END)
            update_cart()
            cartui.update()
            tkinter.messagebox.showinfo(title="Success", message="Remove Success!")
        else:
            tkinter.messagebox.showerror(title="Error", message="Error!")
    else:
        tkinter.messagebox.showerror(title="Error", message="Input refcode!/No cart!")
# --------------------- Create GUI ----------------------- #
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
txtbox = Text(cartui, height=12, width=40, font=txtbox_font)
txtbox.pack(anchor="center")
if txtbox.get("1.0", "end-1c") == "":
    for i in response:
        txtbox.insert(END, i + "\n")
    txtbox.config(state="disabled")

Button(text="Enroll", font=normal_font, command=enroll).pack(anchor="center")
ent = Entry(cartui, font=txtbox_font)
ent.place(x=100, y=450)
Button(text="Remove", font=normal_font, command=remove_cart).place(x=300, y=440)

cartui.mainloop()
