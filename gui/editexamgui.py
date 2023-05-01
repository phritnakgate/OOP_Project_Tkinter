import requests
from tkinter import *
from tkinter.font import Font
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class ExamEditor:
     def __init__(self,refcode):
          self.__refcode = refcode
          self.root = ctk.CTkToplevel()
          self.root.title("Update Exam")
          self.__header_font = ctk.CTkFont(family="Kanit", weight="bold", size=25)
          self.__normal_font = ctk.CTkFont(family="Kanit", weight="normal", size=15)
          self.create_widgets()
          self.root.mainloop()
          
     def create_widgets(self):
        ctk.CTkLabel(self.root, text="Question Number :",font=self.__header_font).grid(row=0, column=0, padx=20, pady=20, sticky=W)
        self.question_number_entry = ctk.CTkEntry(self.root)
        self.question_number_entry.grid(row=0, column=1, padx=20, pady=20)

        ctk.CTkLabel(self.root, text="New Question :",font=self.__header_font).grid(row=1, column=0, padx=20, pady=20, sticky=W)
        self.ques_entry = ctk.CTkEntry(self.root)
        self.ques_entry.grid(row=1, column=1, padx=20, pady=20)

        ctk.CTkLabel(self.root, text="New Answer :",font=self.__header_font).grid(row=2, column=0, padx=20, pady=20, sticky=W)
        self.ans_entry = ctk.CTkEntry(self.root)
        self.ans_entry.grid(row=2, column=1, padx=20, pady=20)

        submit_button = ctk.CTkButton(self.root, text="Submit", command=self.on_submit, font=self.__normal_font)
        submit_button.grid(row=3, columnspan=2, pady=20)
        
        self.result = ctk.CTkLabel(self.root, text="Result: ", font=self.__normal_font)
        self.result.grid(row=4, columnspan=1, pady=20)

        self.result_label = ctk.CTkLabel(self.root, text="", font=ctk.CTkFont(family="Kanit", weight="normal", size=18))
        self.result_label.grid(row=4, columnspan=2, pady=20)

     def update_exams(self, refcode, question_number,ques, ans):
          url = "http://localhost:8000/" + str(refcode) + "/exam/edit?question_number=" + str(question_number)
          data = {       
                    "question": ques,
                    "answer": ans 
               }
          response = requests.put(url, json=data)
          return response.text
   
     def on_submit(self):
          ref = self.__refcode
          question_number = int(self.question_number_entry.get())
          ques = self.ques_entry.get()
          ans = self.ans_entry.get()
          result = self.update_exams(ref, question_number,ques, ans)
          if result[2:14] == "Exam Updated":
               self.result_label.configure(text=result[2:14], text_color="green")
          else:
              self.result_label.configure(text=result[2:11], text_color="red") 

if __name__ == "__main__":
    app = ExamEditor("SOFT001") # เปลี่ยน refcode ตรงนี้ถ้าเอาไปเชื่อมกับระบบอื่น
