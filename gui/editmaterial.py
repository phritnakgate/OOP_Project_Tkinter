import customtkinter as ctk
import requests
import json
from functools import partial

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class EditMaterial:
    def __init__(self, refcode):
        self.__refcode = refcode
        self.__chapter = []
        self.__edmat = ctk.CTkToplevel()
        self.__header_font = ctk.CTkFont(family="Kanit", weight="bold", size=20)
        self.__normal_font = ctk.CTkFont(family="Kanit", weight="normal", size=16)
        self.__txtbox_font = ctk.CTkFont(family="Kanit", weight="normal", size=12)
        self.__edmat.title("Edit Material")
        self.__edmat.geometry("400x400")
        ctk.CTkLabel(self.__edmat, text="Edit Material for "+refcode, font=self.__header_font).pack()
        self.get_chapter()
        self.__combobox_var = ctk.StringVar()
        self.__combobox = ctk.CTkComboBox(master=self.__edmat,
                                    values=self.__chapter,
                                   command=self.get_material,
                                    variable=self.__combobox_var)
        self.__combobox.pack(padx=20, pady=10)
        self.__ent = ctk.CTkTextbox(self.__edmat, height=250, width=250, font=self.__txtbox_font)
        self.__ent.pack(anchor="center")
        ctk.CTkButton(self.__edmat, text="Save", font=self.__txtbox_font,
                      command=lambda: self.save(self.__chapter.index(self.__combobox_var.get()), self.__ent.get("0.0", "end-1c"))).pack()
        self.__edmat.mainloop()


    def load_data(self):
        r = requests.get("http://127.0.0.1:8000/courses/" + self.__refcode)
        data = json.loads(r.text)
        return data
    def get_chapter(self):
        data = self.load_data()
        for i in data['_Courses__chapter']:
            self.__chapter.append(i['_CourseChapter__title'])
        print(self.__chapter)

    def get_material(self, ch):
        print(ch)
        data = self.load_data()
        for i in data['_Courses__chapter']:
            if i['_CourseChapter__title'] == ch:
                print(i['_CourseChapter__material'][0]['_CourseMaterial__material'])
                self.__ent.delete("0.0", "end")
                self.__ent.insert("0.0", i['_CourseChapter__material'][0]['_CourseMaterial__material'])
    def save(self, chap, newmat):
        url = "http://127.0.0.1:8000/courses/"+self.__refcode+"/"+str(chap)+"/modify?newmat="+newmat
        requests.put(url)
        #print(json.loads(r.text))

#EditMaterial("SOFT001")