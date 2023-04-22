from tkinter import *
from tkinter.font import *
import tkinter.messagebox
import customtkinter
import requests
import json

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class CartGUI:
    def __init__(self, username):
        self.__username = username
        self.__response = []
        self.update_cart()
        # --------------------- Create GUI ----------------------- #
        self.__cartui = customtkinter.CTkToplevel()
        self.__header_font = customtkinter.CTkFont(family="Kanit", weight="bold", size=20)
        self.__normal_font = customtkinter.CTkFont(family="Kanit", weight="normal", size=16)
        self.__txtbox_font = customtkinter.CTkFont(family="Kanit", weight="normal", size=12)
        self.__cartui.title("Cart")
        self.__cartui.geometry("500x600")
        self.__cartui.resizable(width=False, height=False)

        # self.__menuitem = Menu()
        # self.__menuitem.add_cascade(label='Your Account: ' + str(self.__username))
        # self.__menuitem.add_cascade(label='About')
        # self.__menuitem.add_cascade(label='Exit')
        # self.__cartui.config(menu=self.__menuitem)

        customtkinter.CTkLabel(self.__cartui, text="Cart", font=self.__header_font).pack(anchor="center")
        customtkinter.CTkButton(self.__cartui, text="Refresh Cart", font=self.__normal_font, command=self.refresh).pack(anchor="e")
        self.__txtbox = customtkinter.CTkTextbox(self.__cartui, height=400, width=400, font=self.__txtbox_font)
        self.__txtbox.pack(anchor="center")
        if self.__txtbox.get("1.0", "end-1c") == "":
            for i in self.__response:
                self.__txtbox.insert(END, i + "\n")
            self.__txtbox.configure(state="disabled")

        customtkinter.CTkButton(self.__cartui, text="Enroll", font=self.__normal_font, command=self.enroll).pack(anchor="center")
        customtkinter.CTkLabel(self.__cartui, text="Remove Cart", font=self.__normal_font).pack(anchor="center")
        self.__ent = customtkinter.CTkEntry(self.__cartui, font=self.__txtbox_font)
        self.__ent.pack(anchor="center")
        customtkinter.CTkButton(self.__cartui, text="Remove", font=self.__normal_font, command=self.remove_cart).pack(anchor="center")

        self.__cartui.mainloop()

    def update_cart(self):
        r = requests.get("http://localhost:8000/cart")
        data = json.loads(r.text)
        cart_item = data["Cart"]
        if cart_item:
            display = []
            for i in cart_item:
                cart_list = i['_Courses__refcode'] + ":" + i['_Courses__title']
                display.append(cart_list)
            self.__response = display
        else:
            self.__response = ['No course in cart']
    def enroll(self):
        url = "http://localhost:8000/enroll?user=" + str(self.__username)
        if self.__response != ['No course in cart']:
            requests.post(url)
            tkinter.messagebox.showinfo(title="Success", message="Enroll Success!")
            self.__cartui.destroy()
        else:
            tkinter.messagebox.showerror(title="Error", message="Cart is Empty!")

    def refresh(self):
        self.update_cart()
        print(self.__response)
        self.__txtbox.configure(state="normal")
        self.__txtbox.delete("1.0", "end-1c")
        for j in self.__response:
            self.__txtbox.insert(END, j + "\n")
        self.__txtbox.configure(state="disabled")

    def remove_cart(self):
        ref = self.__ent.get()
        print(ref)
        if ref != "" and self.__response != ['No course in cart']:
            req = {"refcode": str(ref)}
            r = requests.post("http://localhost:8000/removecart", json=req)
            res = r.text
            print(res)
            if res == "{\"Success\":\"Remove complete\"}":
                self.__ent.delete(0, END)
                self.update_cart()
                self.__cartui.update()
                tkinter.messagebox.showinfo(title="Success", message="Remove Success!")
            else:
                tkinter.messagebox.showerror(title="Error", message="Error!")
        else:
            tkinter.messagebox.showerror(title="Error", message="Input refcode!/No cart!")

#CartGUI("ffwatcharin")