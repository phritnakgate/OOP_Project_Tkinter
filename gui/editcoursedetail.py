import customtkinter as ctk
import requests
import json

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class EditCourseDetailGUI:
    def __init__(self, refcode):
        self.__refcode = refcode
        self.__root = ctk.CTk()
        self.__root.title("Edit Course Detail")
        self.__root.geometry("600x600")
        self.__edited_data = None
        self.__header_font = ctk.CTkFont(family="Kanit", weight="bold", size=30)
        self.__normal_font = ctk.CTkFont(family="Kanit", weight="normal", size=15)
        self.find_course()
        self.create_widgets()
        self.__root.mainloop()

    def create_widgets(self):
        title_label = ctk.CTkLabel(self.__root, text="Edit Course Detail", font=self.__header_font)
        title_label.pack(pady=10)

        form_frame = ctk.CTkFrame(self.__root)
        form_frame.pack(pady=20)

        self.entries = [
            ctk.CTkEntry(form_frame, placeholder_text="Refcode", font=self.__normal_font),
            ctk.CTkEntry(form_frame, placeholder_text="Title", font=self.__normal_font),
            ctk.CTkEntry(form_frame, placeholder_text="Description", font=self.__normal_font),
            ctk.CTkEntry(form_frame, placeholder_text="Teacher", font=self.__normal_font),
            ctk.CTkEntry(form_frame, placeholder_text="Category", font=self.__normal_font),
            ctk.CTkEntry(form_frame, placeholder_text="Target Audience", font=self.__normal_font),
            ctk.CTkEntry(form_frame, placeholder_text="Objective", font=self.__normal_font),
            ctk.CTkEntry(form_frame, placeholder_text="Hours", font=self.__normal_font),
            ctk.CTkEntry(form_frame, placeholder_text="Recommended Hours",
                         font=ctk.CTkFont(family="Kanit", weight="normal", size=13)),
            ctk.CTkEntry(form_frame, placeholder_text="Contact Email", font=self.__normal_font)
        ]

        for entry in self.entries:
            entry.pack(fill='x', padx=10, pady=5)
        run = 0
        for key, value in self.__edited_data.items():
            if run <= 8:
                self.entries[run].insert("0", value)
                run += 1
            else:
                break

        self.submit_button = ctk.CTkButton(self.__root, text="Submit", command=self.all_func,
                                           font=ctk.CTkFont(family="Kanit", weight="normal", size=15))
        self.submit_button.pack(pady=10)

        self.message_label = ctk.CTkLabel(self.__root, text="",
                                          font=ctk.CTkFont(family="Kanit", weight="bold", size=20))
        self.message_label.pack(pady=5)

    def submit_course(self):
        course_keys = [
            "refcode", "title", "desc", "teacher", "catg", "target", "objective", "hour", "recom_hour", "contact"
        ]
        course_info = {}
        # Check if any entry is blank
        if all(entry.get() for entry in self.entries):
            for key, entry in zip(course_keys, self.entries):
                if key in ["hour", "recom_hour"]:
                    course_info[key] = int(entry.get())
                else:
                    course_info[key] = entry.get()

            # Use the requests library to send a PUT request here
            url = "http://localhost:8000/"+course_info["refcode"]+"/edit"
            headers = {"Content-Type": "application/json"}
            response = requests.put(url, data=json.dumps(course_info), headers=headers)
            self.message_label.configure(text="Course Modified", text_color="green")
            #   self.__root.destroy()
        else:
            self.message_label.configure(text="Please fill in all fields", text_color="red")

    def find_course(self):
        url = "http://localhost:8000/courses/"+self.__refcode
        r = requests.get(url)
        self.__edited_data = json.loads(r.text)
        print(self.__edited_data)
    def all_func(self):
        self.submit_course()

#EditCourseDetailGUI("HARD001")

