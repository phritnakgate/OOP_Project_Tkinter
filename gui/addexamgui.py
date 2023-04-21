import tkinter as tk
import customtkinter as ctk
from tkinter.font import Font
import requests

class ExamUI:
    def __init__(self, refcode):
        self.__refcode = refcode
        self.root = tk.Tk()
        self.root.title("Exam Management")
        self.root.configure(bg="#ffffff")
        self.font1 = Font(family="Kanit", weight="bold", size=20)
        self.font2 = Font(family="Kanit", weight="bold", size=12)
        self.create_widgets()
        self.root.mainloop()
    
    def create_widgets(self):       
        # Add Questions
        question_label = tk.Label(self.root, text="Question:", font=self.font1, bg="#ffffff", fg="#0066b2")
        question_label.grid(row=0, column=0)
        self.question_entry = ctk.CTkEntry(self.root, bg="#ffffff", fg="#0066b2", insertbackground="#0066b2")
        self.question_entry.grid(row=0, column=1)

        answer_label = tk.Label(self.root, text="Answer:", font=self.font1, bg="#ffffff", fg="#0066b2")
        answer_label.grid(row=1, column=0)
        self.answer_entry = ctk.CTkEntry(self.root, bg="#ffffff", fg="#0066b2", insertbackground="#0066b2")
        self.answer_entry.grid(row=1, column=1)

        add_button = ctk.CTkButton(self.root, text="Add Question", command=self.add_question)
        add_button.grid(row=2, columnspan=2)

        self.result_label = tk.Label(self.root, text="", bg="#ffffff")
        self.result_label.grid(row=3, columnspan=2)

        # Display Exam Questions
        exam_label = tk.Label(self.root, text="Exam Questions:", bg="#ffffff", fg="#0066b2")
        exam_label.grid(row=4, column=0)

        self.exam_questions = tk.Text(self.root,font=self.font2, wrap=tk.WORD, height=10, width=50, bg="#ffffff", fg="#0066b2", insertbackground="#0066b2")
        self.exam_questions.grid(row=5, columnspan=2)

        get_button = ctk.CTkButton(self.root, text="Get Exam Questions", command=self.get_exam_questions)
        get_button.grid(row=6, columnspan=2)

    def add_question(self):
        data = {  
            "questions": [
                {
                    "question": self.question_entry.get(),
                    "answer": self.answer_entry.get()
                }
            ]
        }
        response = requests.post("http://127.0.0.1:8000/exam/question_and_answer?refcode="+str(self.__refcode), json=data)
        self.result_label.config(text=response.text)
        self.get_exam_questions()

    def get_exam_questions(self):
        response = requests.get("http://127.0.0.1:8000/exam?refcode="+str(self.__refcode))
        self.exam_questions.delete(1.0, tk.END)
        for q in response.json():
            self.exam_questions.insert(tk.END, f"Question : {q['_ExamItem__question']}, Answer : {q['_ExamItem__answer']}\n")
 
ExamUI("SOFT001") # เปลี่ยน refcode ตรงนี้ถ้าเอาไปเชื่อมกับระบบอื่น