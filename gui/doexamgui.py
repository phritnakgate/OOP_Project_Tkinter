import customtkinter as ctk
import requests

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class DoingExamUI:   
    def __init__(self, user, refcode):
        self.__refcode = refcode
        self.__data = self.get_exam_questions()
        self.__user = user
        self.__root = ctk.CTkToplevel()
        self.__root.title("Doing Exam")
        self.screen(600,400)
        self.__root.resizable(width=False, height=False)
        self.__header_font = ctk.CTkFont(family="Kanit", weight="bold", size=25)
        self.__normal_font = ctk.CTkFont(family="Kanit", weight="normal", size=15)
        self.current_question = 0
        self.user_answers = [""] * len(self.__data)
        
        if len(self.__data) == 0:
            self.show_no_questions()
        else:
            self.create_widgets()
        
        self.__root.mainloop()
    
    def screen(self, width, height):
        self.screen_width = self.__root.winfo_screenwidth()
        self.screen_height = self.__root.winfo_screenheight()             
        self.x = (self.screen_width // 2) - (width // 2)
        self.y = (self.screen_height // 2) - (height // 2)
        self.__root.geometry(f"{width}x{height}+{self.x}+{self.y}")
        
    def get_exam_questions(self):
        response = requests.get("http://127.0.0.1:8000/exam?refcode=" + str(self.__refcode))
        return response.json()
    
    def submit_exam(self, data):
        url = f"http://127.0.0.1:8000/courses/{self.__user}/{self.__refcode}/exam/do_exam"
        response = requests.post(url, json=data)
        return response.json()
    
    def show_no_questions(self):
        self.no_questions_label = ctk.CTkLabel(self.__root, 
                                               text="There are no exam on this subject yet.",
                                               font=self.__header_font)
        self.no_questions_label.pack(pady=40)

        self.exit_button = ctk.CTkButton(self.__root, text="Exit",
                                         command=self.__root.destroy,
                                         font=self.__normal_font)
        self.exit_button.pack(side=ctk.TOP, padx=10, pady=10)
        
    def create_widgets(self):
        self.question_label = ctk.CTkLabel(self.__root,
                                           text=self.__data[self.current_question]["_ExamItem__question"],
                                           font=self.__header_font)
        self.question_label.pack(pady=30)

        self.answer_entry = ctk.CTkEntry(self.__root,
                                         font=self.__normal_font,
                                         width=350)
        self.answer_entry.pack(pady=10)

        self.prev_button = ctk.CTkButton(self.__root, 
                                         text="Previous Question",
                                         font=self.__normal_font,
                                         command=self.show_previous_question)
        self.prev_button.pack(side=ctk.LEFT, padx=20, pady=15)
        
        self.next_button = ctk.CTkButton(self.__root,
                                         text="Next Question",
                                         font=self.__normal_font,
                                         command=self.show_next_question)
        self.next_button.pack(side=ctk.RIGHT, padx=20, pady=15)

        self.update_buttons()

    def show_previous_question(self):
        self.user_answers[self.current_question] = self.answer_entry.get()
        self.current_question -= 1
        self.update_question()
        self.update_buttons()

    def show_next_question(self):
        self.user_answers[self.current_question] = self.answer_entry.get()
        self.current_question += 1
        self.update_question()
        self.update_buttons()

    def update_question(self):
        self.question_label.configure(text=self.__data[self.current_question]["_ExamItem__question"])
        self.answer_entry.delete(0, ctk.END)
        self.answer_entry.insert(0, self.user_answers[self.current_question])

    def update_buttons(self):
        if self.current_question == 0:
            self.prev_button.configure(state=ctk.DISABLED)
        else:
            self.prev_button.configure(state=ctk.NORMAL)

        if self.current_question == len(self.__data) - 1:
            self.next_button.configure(text="Submit", command=self.submit_answers)
        else:
            self.next_button.configure(text="Next Question", command=self.show_next_question)

    def submit_answers(self):
        self.user_answers[self.current_question] = self.answer_entry.get()
        
        result = self.submit_exam(self.user_answers)
        percent_string = result[0]
        percent_float = float(percent_string.strip('%'))

        self.question_label.configure(text=f"You have submitted your answers!")
        self.answer_entry.pack_forget()

        self.result_label = ctk.CTkLabel(self.__root, 
                                         text=f"Your progression is: {result[0]}", 
                                         text_color="green",
                                         font=ctk.CTkFont(family="Kanit", weight="normal", size=20))
        self.result_label.pack(side=ctk.TOP)
        if percent_float < 50.0:
            self.result_label.configure(text_color="red")

        self.prev_button.pack_forget()
        self.next_button.pack(side=ctk.BOTTOM, pady=50)
        self.next_button.configure(text="Exit", 
                                   command=self.__root.destroy)

             
#DoingExamUI("ffwatcharin", "SOFT001") # เปลี่ยน user,refcode ตรงนี้ถ้าเอาไปเชื่อมกับระบบอื่น