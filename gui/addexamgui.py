import customtkinter as ctk
from tkinter import *
import requests

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class AddingExamUI:
    def __init__(self, refcode):
        self.__refcode = refcode
        self.root = ctk.CTkToplevel()
        self.root.title("Exam Management")
        self.screen(600, 400)
        self.root.resizable(width=False, height=False)
        self.__header_font = ctk.CTkFont(family="Kanit", weight="bold", size=25)
        self.__normal_font = ctk.CTkFont(family="Kanit", weight="normal", size=15)
        self.__txtbox_font = ctk.CTkFont(family="Kanit", weight="normal", size=13)
        self.create_widgets()
        self.root.mainloop()
        
    def screen(self, width, height):
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()             
        self.x = (self.screen_width // 2) - (width // 2)
        self.y = (self.screen_height // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{self.x}+{self.y}")
    
    def create_widgets(self):       
        # Configure rows and columns for resizing
        for i in range(10):
            self.root.rowconfigure(i, weight=1)
        for i in range(2):
            self.root.columnconfigure(i, weight=1)
        
        # Add Questions
        self.question_label = ctk.CTkLabel(self.root, text="Question :", font=self.__header_font)
        self.question_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.question_entry = ctk.CTkEntry(self.root,height=45)
        self.question_entry.grid(row=0, column=1, sticky="ew", padx=10, pady=10)

        self.answer_label = ctk.CTkLabel(self.root, text="Answer :", font=self.__header_font)
        self.answer_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)
        self.answer_entry = ctk.CTkEntry(self.root,height=45)
        self.answer_entry.grid(row=2, column=1, sticky="ew", padx=10, pady=10)

        self.add_button = ctk.CTkButton(self.root, text="Add Question", command=self.add_question,height=40,font=self.__txtbox_font)
        self.add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.result_label = ctk.CTkLabel(self.root, text="", font=self.__txtbox_font, text_color="green")
        self.result_label.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

        # Display Exam Questions
        self.exam_label = ctk.CTkLabel(self.root, text="Exam Questions and Answer :", font=self.__header_font)
        self.exam_label.grid(row=6, column=0, sticky="w", padx=10, pady=10)

        self.exam_questions = ctk.CTkTextbox(self.root, font=self.__normal_font, wrap="word", height=150, width=5)
        self.exam_questions.grid(row=7, column=0, columnspan=2, sticky="nsew", padx=10)

        self.get_button = ctk.CTkButton(self.root, text="Get Exam", command=self.get_exam_questions,height=40,font=self.__txtbox_font)
        self.get_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

    def add_question(self):
        data = {  
            "questions": [
                {
                    "question": self.question_entry.get(),
                    "answer": self.answer_entry.get()
                }
            ]
        }
        response = requests.post("http://127.0.0.1:8000/exam/question_and_answer?refcode="+ str(self.__refcode), json=data)
        self.result_label.configure(text=response.text[2:16])
        self.get_exam_questions()

    def get_exam_questions(self):
        response = requests.get("http://127.0.0.1:8000/exam?refcode="+ str(self.__refcode))
        self.exam_questions.delete(1.0, ctk.END)
        for q in response.json():
            self.exam_questions.insert(ctk.END, f"Question : {q['_ExamItem__question']}   |   Answer : {q['_ExamItem__answer']}\n")
 
AddingExamUI("SOFT001") # เปลี่ยน refcode ตรงนี้ถ้าเอาไปเชื่อมกับระบบอื่น