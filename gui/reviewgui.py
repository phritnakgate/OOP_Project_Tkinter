from tkinter import *
from tkinter import messagebox
from tkinter.font import *
import requests
import json
from tkinter import ttk

class ReviewGUI:
    def __init__(self, refcode):
        self.__refcode = refcode
        self.__review = Tk()    #When merge change to Toplevel()
        self.__header_font = Font(family="Kanit", weight="bold", size=20)
        self.__normal_font = Font(family="Kanit", weight="normal", size=16)
        self.__txtbox_font = Font(family="Kanit", weight="normal", size=12)
        self.__review.title("Review Course")
        self.__review.geometry("400x500")
        Label(text="Review", font=self.__header_font).pack(anchor="center")
        Label(text="Currently Review: "+self.__refcode, font=self.__txtbox_font).pack(anchor="center")
        Label(text="Rating", font=self.__normal_font).pack(anchor="center")
        self.__rate = StringVar()
        self.__ratingchoose = ttk.Combobox(self.__review, width=5, textvariable=self.__rate)
        self.__ratingchoose['value']=(1,2,3,4,5)
        self.__ratingchoose.pack(anchor="center")
        Label(text="Review", font=self.__normal_font).pack(anchor="center")
        self.__txtrev = Text(font=self.__txtbox_font, width=30, height=5)
        self.__txtrev.pack(anchor="center")
        Button(text="Write a review", font=self.__txtbox_font, command=self.write_a_review).pack(anchor="center")
        self.__review.mainloop()
    def write_a_review(self):
        data = {
            "score": self.__rate.get(),
            "comment": self.__txtrev.get("1.0","end-1c"),
            "refcode": self.__refcode
        }
        r = requests.post("http://127.0.0.1:8000/add_review", json=data)
        resp = json.loads(r.text)
        if resp == {'status': 'Add Success'}:
            messagebox.showinfo(title="Success!", message="Review Added")
            self.__review.destroy()
        else:
            messagebox.showerror(title="Err", message=str(resp))
ReviewGUI("SOFT001")