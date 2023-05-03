import customtkinter as ctk
import requests
import json

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class CourseChapterCreator:
    def __init__(self, refcode):
        self.__refcode = refcode
        self._root = ctk.CTk()
        self._root.title("Course Chapter Creator")
        self._root.geometry("500x500")
        self._root.columnconfigure(0, weight=1)
        self._root.columnconfigure(1, weight=1)
        self.__header_font = ctk.CTkFont(family="Kanit", weight="bold", size=30)
        self.__normal_font = ctk.CTkFont(family="Kanit", weight="normal", size=15)
        self.create_widgets()
        self._root.mainloop()

    def create_widgets(self):             
     for i in range(5):
          self._root.rowconfigure(i, weight=1)

     self._root.columnconfigure(0, weight=1)
     self._root.columnconfigure(1, weight=1)
     self._root.columnconfigure(2, weight=1)

     self.title = ctk.CTkLabel(self._root, text="Create Chapter", font=self.__header_font)
     self.title.grid(row=0, column=0, columnspan=3)

     self.chapter_label = ctk.CTkLabel(self._root, text="Number of Chapter:", font=self.__normal_font)
     self.chapter_label.grid(row=1, column=0, padx=20, sticky="se")
     self.chapter_entry = ctk.CTkEntry(self._root, width=50)
     self.chapter_entry.grid(row=1, column=1, padx=20, sticky="sw")

     self.next_button = ctk.CTkButton(self._root, text="Next", command=self.submit_data,font=self.__normal_font)
     self.next_button.grid(row=2, column=0, columnspan=3, pady=10)

     self.result_label = ctk.CTkLabel(self._root, text="Result:",font=self.__normal_font)
     self.result_label.grid(row=3, column=0, columnspan=3)
     
     self.result = ctk.CTkLabel(self._root, text= "", font=self.__normal_font)
     self.result.grid(row=3, column=1, columnspan=3, pady=20)


    def submit_data(self):
        if not self.chapter_entry.get().strip():
            self.result.configure(text="Please fill", text_color="red")
            return
        else:
            self.result.configure(text="Correct", text_color="green")

        num_chapter = int(self.chapter_entry.get())

        self.titles = []
        self.materials = []

        self.canvas = ctk.CTkCanvas(self._root, bg="#242424", highlightthickness=0)
        self.scrollbar = ctk.CTkScrollbar(self._root, orientation="vertical", command=self.canvas.yview)
        self.scrollable_frame = ctk.CTkFrame(self.canvas)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=4, column=4, rowspan=num_chapter+1, sticky="ns")
        self.canvas.grid(row=4, column=0, rowspan=num_chapter+1, columnspan=4, sticky="nsew", padx=(50, 0), pady=20)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        for i in range(num_chapter):
            title_label = ctk.CTkLabel(self.scrollable_frame, text=f"Title {i+1}:", font=self.__normal_font)
            title_label.grid(row=i, column=0, padx=20, pady=5, sticky="e")
            self.titles.append(ctk.CTkEntry(self.scrollable_frame, width=100, font=self.__normal_font))
            self.titles[-1].grid(row=i, column=1, padx=(0, 20), pady=5, sticky="w")

            material_label = ctk.CTkLabel(self.scrollable_frame, text=f"Material {i+1}:", font=self.__normal_font)
            material_label.grid(row=i, column=2, padx=(0, 20), pady=5, sticky="e")
            self.materials.append(ctk.CTkEntry(self.scrollable_frame, width=100, font=self.__normal_font))
            self.materials[-1].grid(row=i, column=3, padx=(0, 20), pady=5, sticky="w")

        self.submit_button = ctk.CTkButton(self._root, text="Submit", command=self.send_data, font=self.__normal_font)
        self.submit_button.grid(row=num_chapter+5, column=0, columnspan=3, pady=20)


    def send_data(self):
        titles_data = [title.get() for title in self.titles]
        materials_data = [material.get() for material in self.materials]

        data = {
            "titles": titles_data,
            "materials": materials_data}

        refcode = self.__refcode
        response = requests.post(f"http://localhost:8000/courses/{refcode}/create_chapter", json=data)
        self.result_label.configure(text=f"Result: {response.status_code}")
        
class CourseGUI:
    def __init__(self):
        self.__root = ctk.CTk()
        self.__root.title("Create Course")
        self.__root.geometry("600x600")
        self.__header_font = ctk.CTkFont(family="Kanit", weight="bold", size=30)
        self.__normal_font = ctk.CTkFont(family="Kanit", weight="normal", size=15)
        self.create_widgets()        
        self.__root.mainloop()

    def create_widgets(self):
        title_label = ctk.CTkLabel(self.__root, text="Create Course", font=self.__header_font)
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
            ctk.CTkEntry(form_frame, placeholder_text="Recommended Hours", font=ctk.CTkFont(family="Kanit", weight="normal", size=13)),
            ctk.CTkEntry(form_frame, placeholder_text="Contact Email", font=self.__normal_font)
        ]
        
        for entry in self.entries:
            entry.pack(fill='x', padx=10, pady=5)

        self.submit_button = ctk.CTkButton(self.__root, text="Submit", command=self.all_func, font=ctk.CTkFont(family="Kanit", weight="normal", size=15))
        self.submit_button.pack(pady=10)

        self.message_label = ctk.CTkLabel( self.__root, text="", font=ctk.CTkFont(family="Kanit", weight="bold", size=20))
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

            # Use the requests library to send a POST request here
            url = "http://localhost:8000/create_course"
            headers = {"Content-Type": "application/json"}
            response = requests.post(url, data=json.dumps(course_info), headers=headers)
            self.message_label.configure(text="Course created", text_color="green")    
          #   self.__root.destroy()                  
        else:
            self.message_label.configure(text="Please fill in all fields", text_color="red")     
                  
    def all_func(self):        
         self.submit_course() 
         CourseChapterCreator(self.entries[0].get())
         
                                           
# CourseGUI()
# CourseChapterCreator("SOFT001")

