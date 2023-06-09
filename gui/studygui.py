# This file should execute from mycoursegui #
from tkinter import *
from tkinter.font import *
import tkinter.messagebox
import customtkinter
import requests
import json
from functools import partial

from gui.doexamgui import DoingExamUI

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")


class Study:
    def __init__(self, user, refcode):
        self.__user = user
        self.__refcode = refcode
        self.__posy = 50
        
        # --------------------- Create GUI ----------------------- #
        self.__study = customtkinter.CTkToplevel()
        self.__header_font = customtkinter.CTkFont(family="Kanit", weight="bold", size=20)
        self.__normal_font = customtkinter.CTkFont(family="Kanit", weight="normal", size=16)
        self.__txtbox_font = customtkinter.CTkFont(family="Kanit", weight="normal", size=12)
        self.__study.title("My Course")
        self.__study.geometry("700x700")
        # self.__study.resizable(width=False, height=False)
        customtkinter.CTkLabel(self.__study, text=self.get_name(), font=self.__header_font).pack(anchor="center")
        self.__chapter_label = []
        for i in self.get_all_chapter():
            lbl = customtkinter.CTkLabel(self.__study, text=i, font=self.__normal_font)
            lbl.place(x=50, y=self.__posy)
            self.__chapter_label.append(lbl)
            self.__posy += 50
        # print(self.__chapter_label)
        customtkinter.CTkLabel(self.__study, text="Exam", font=self.__normal_font).place(x=50, y=self.__posy)
        self.__posy = 50
        self.__chapter_button = []
        for index, _ in enumerate(self.__chapter_label):
            btn = customtkinter.CTkButton(self.__study, text="Start", font=self.__txtbox_font,
                                          command=partial(self.press_start, index))
            btn.place(x=300, y=self.__posy)
            self.__chapter_button.append(btn)
            self.__posy += 50
        customtkinter.CTkButton(self.__study, text="Take Exam", font=self.__txtbox_font, command=self.take_exam).place(x=300, y=self.__posy)
        self.__study.mainloop()

    def request_url(self):
        url = "http://localhost:8000/courses/" + str(self.__user) + "/" + str(self.__refcode)
        r = requests.get(url)
        data = json.loads(r.text)
        return data

    def get_name(self):
        data = self.request_url()
        # print(data)
        name = data['_Courses__refcode'] + ":" + data['_Courses__title']
        return name

    def get_all_chapter(self):
        data = self.request_url()
        chapter = data['_Courses__chapter']
        title = []
        for i in chapter:
            title.append(i["_CourseChapter__title"])
        # print(title)
        return title

    def get_material(self, chapter):
        title = self.get_all_chapter()
        # print(chapter)
        chapterno = title.index(chapter)
        url = "http://localhost:8000/courses/" + str(self.__user) + "/" + str(self.__refcode) + "/" + str(chapterno)
        # print(url)
        r = requests.get(url)
        data = json.loads(r.text)
        material = data["_CourseChapter__material"][0]["_CourseMaterial__material"]
        return material

    def press_start(self, index):
        title = self.get_all_chapter()
        chapter = index
        mat = self.get_material(title[chapter])
        txtbox = customtkinter.CTkTextbox(self.__study, font=self.__txtbox_font, width=500, height=250)
        txtbox.place(x=100, y=400)
        if txtbox.get("1.0", "end-1c") == "":
            txtbox.insert(INSERT, str(mat))
            txtbox.configure(state="disabled")
        else:
            txtbox.configure(state="normal")
            txtbox.delete("1.0", "end-1c")
            txtbox.insert(INSERT, str(mat))
            txtbox.configure(state="disabled")

    def take_exam(self):
        DoingExamUI(self.__user, self.__refcode)

#Study("ffwatcharin","SOFT001")