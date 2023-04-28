from tkinter import *
from tkinter import messagebox
import customtkinter
import requests
import json
from tkinter import ttk

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

class ReviewGUI:
    def __init__(self, username, refcode):
        self.__username = username
        self.__refcode = refcode

        self.__review = customtkinter.CTkToplevel()  # When merge change to Toplevel()
        self.__header_font = customtkinter.CTkFont(family="Kanit", weight="bold", size=20)
        self.__normal_font = customtkinter.CTkFont(family="Kanit", weight="normal", size=16)
        self.__txtbox_font = customtkinter.CTkFont(family="Kanit", weight="normal", size=12)
        self.__review.title("Review Course")
        self.__review.geometry("400x500")
        customtkinter.CTkLabel(self.__review, text="Review", font=self.__header_font).pack(anchor="center")
        customtkinter.CTkLabel(self.__review, text="Currently Review: " + self.__refcode, font=self.__header_font).pack(anchor="center")
        customtkinter.CTkLabel(self.__review, text="Rating", font=self.__normal_font).pack(anchor="center")
        self.__ratingchoose = customtkinter.CTkOptionMenu(self.__review, width=20, values=['1', '2', '3', '4', '5'])
        self.__ratingchoose.pack(anchor="center")
        customtkinter.CTkLabel(self.__review, text="Review", font=self.__normal_font).pack(anchor="center")
        self.__txtrev = customtkinter.CTkTextbox(self.__review, font=self.__txtbox_font, width=300, height=300)
        self.__txtrev.pack(anchor="center")
        customtkinter.CTkButton(self.__review, text="Write a review", font=self.__txtbox_font, command=self.write_a_review).pack(anchor="center")
        self.__review.mainloop()

    def write_a_review(self):
        data = {
            "user": self.__username,
            "score": int(self.__ratingchoose.get()),
            "comment": self.__txtrev.get("1.0", "end-1c"),
            "refcode": self.__refcode
        }
        r = requests.post("http://127.0.0.1:8000/add_review", json=data)
        resp = json.loads(r.text)
        if resp == {'status': 'Add Success'}:
            messagebox.showinfo(title="Success!", message="Review Added")
            self.__review.destroy()
        else:
            messagebox.showerror(title="Err", message=str(resp))


#ReviewGUI("ffwatcharin", "SOFT001")
