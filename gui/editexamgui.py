import requests
from tkinter import *
import tkinter as tk
from tkinter.font import Font
import customtkinter as ctk


class ExamEditor:
     def __init__(self,refcode):
          self.__refcode = refcode
          self.root = Tk()
          self.root.title("Update Exam")
          self.root.configure(bg="#ffffff")
          self.font1 = Font(family="Kanit", weight="bold", size=20)
          self.create_widgets()
          self.root.mainloop()
          
     def create_widgets(self):
        tk.Label(self.root, text="Question Number :",font=self.font1 ,bg="#ffffff", fg="#0066b2").grid(row=0, column=0, padx=20, pady=20, sticky=W)
        self.question_number_entry = ctk.CTkEntry(self.root)
        self.question_number_entry.grid(row=0, column=1, padx=20, pady=20)

        tk.Label(self.root, text="New Question :",font=self.font1, bg="#ffffff", fg="#0066b2").grid(row=1, column=0, padx=20, pady=20, sticky=W)
        self.ques_entry = ctk.CTkEntry(self.root)
        self.ques_entry.grid(row=1, column=1, padx=20, pady=20)

        tk.Label(self.root, text="New Answer :",font=self.font1 ,bg="#ffffff", fg="#0066b2").grid(row=2, column=0, padx=20, pady=20, sticky=W)
        self.ans_entry = ctk.CTkEntry(self.root)
        self.ans_entry.grid(row=2, column=1, padx=20, pady=20)

        submit_button = ctk.CTkButton(self.root, text="Submit", command=self.on_submit, text_color="#ffffff")
        submit_button.grid(row=3, columnspan=2, pady=20)

        self.result_label = tk.Label(self.root, text="Result:", bg="#ffffff", fg="black")
        self.result_label.grid(row=4, columnspan=2, pady=20)

     def update_exams(self, refcode, question_number,ques, ans):
          url = "http://localhost:8000/exam/edit?refcode=" + str(refcode) +"&question_number="+ str(question_number)
          data = {       
                    "question": ques,
                    "answer": ans 
               }
          response = requests.put(url, json=data)
          return response.json()
   
     def on_submit(self):
          ref = self.__refcode
          question_number = int(self.question_number_entry.get())
          ques = self.ques_entry.get()
          ans = self.ans_entry.get()
          result = self.update_exams(ref, question_number,ques, ans)
          self.result_label.config(text=f"Result: {result}")

if __name__ == "__main__":
    app = ExamEditor("SOFT001") # เปลี่ยน refcode ตรงนี้ถ้าเอาไปเชื่อมกับระบบอื่น
