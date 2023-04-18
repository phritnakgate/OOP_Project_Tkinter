import tkinter as tk
import customtkinter as ctk
from tkinter.font import Font
import requests

def add_question():
    data = {
            "questions": [
                    {
                        "question": question_entry.get(),
                        "answer": answer_entry.get()
                    }
                ]
            }
    response = requests.post("http://127.0.0.1:8000/exam/question_and_answer", json=data)

def get_exam_questions():
    response = requests.get("http://127.0.0.1:8000/exam")
    print(response.text)
    exam_questions.delete(1.0, tk.END)
    for q in response.json():
        exam_questions.insert(tk.END, f"Question : {q['_ExamItem__question']}, Answer : {q['_ExamItem__answer']}\n")

root = tk.Tk()
root.title("Exam Management")
root.configure(bg="#ffffff")

# Add Questions
font1 = Font(family="Kanit", weight="bold", size=20)
font2 = Font(family="Kanit", weight="bold", size=12)
question_label = tk.Label(root, text="Question:", font=font1, bg="#ffffff", fg="#0066b2")
question_label.grid(row=0, column=0)
question_entry = ctk.CTkEntry(root, bg="#ffffff", fg="#0066b2", insertbackground="#0066b2")
question_entry.grid(row=0, column=1)

answer_label = tk.Label(root, text="Answer:", font=font1, bg="#ffffff", fg="#0066b2")
answer_label.grid(row=1, column=0)
answer_entry = ctk.CTkEntry(root, bg="#ffffff", fg="#0066b2", insertbackground="#0066b2")
answer_entry.grid(row=1, column=1)

add_button = ctk.CTkButton(root, text="Add Question", command=add_question)
add_button.grid(row=2, columnspan=2)

result_label = tk.Label(root, text="", bg="#ffffff")
result_label.grid(row=3, columnspan=2)

# Display Exam Questions
exam_label = tk.Label(root, text="Exam Questions:", bg="#ffffff", fg="#0066b2")
exam_label.grid(row=4, column=0)

exam_questions = tk.Text(root,font=font2, wrap=tk.WORD, height=10, width=50, bg="#ffffff", fg="#0066b2", insertbackground="#0066b2")
exam_questions.grid(row=5, columnspan=2)

get_button = ctk.CTkButton(root, text="Get Exam Questions", command=get_exam_questions)
get_button.grid(row=6, columnspan=2)

root.mainloop()
