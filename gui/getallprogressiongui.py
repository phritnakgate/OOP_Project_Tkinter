import requests
import customtkinter as ctk


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class AllProgression:
    def __init__(self, name):
        self.__name = name
        self.__root = ctk.CTk()
        self.__root.title("Your All Progression")
        self.__root.geometry("550x400")
        self.__header_font = ctk.CTkFont(family="Kanit", weight="bold", size=30)
        self.__normal_font = ctk.CTkFont(family="Kanit", weight="normal", size=15)
        
        
        self.title = ctk.CTkLabel(self.__root, text="Your All Progression", font=self.__header_font)
        self.title.pack(side=ctk.TOP)

     #    self.label = ctk.CTkLabel(self.__root, text="Enter your username:",font=self.__normal_font)
     #    self.label.pack(pady=10)

     #    self.entry = ctk.CTkEntry(self.__root,font=self.__normal_font)
     #    self.entry.pack(pady=10)

     #    self.submit_button = ctk.CTkButton(self.__root, text="Get Progression", command=self.on_submit,font=self.__normal_font)
     #    self.submit_button.pack(pady=10)

        self.progression_frame = ctk.CTkFrame(self.__root)
        self.progression_frame.pack(pady=10)
        self.on_submit()
        
        self.__root.mainloop()

    def get_all_progression(self, user):
        url = f"http://localhost:8000/{self.__name}/get_all_grogression"
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}"

    def on_submit(self):
     #    user = self.entry.get()
        progression_data = self.get_all_progression(self.__name)
        self.display_progression(progression_data)
        
    def ref_2_name(self, refcode):
          url = f"http://localhost:8000/courses/{refcode}" # replace with the actual URL of the endpoint
          response = requests.get(url)
          return response.json()

    def display_progression(self, progression_data):
        for widget in self.progression_frame.winfo_children():
            widget.destroy()

        for course in progression_data:
            course_code = self.ref_2_name(course["_CourseProgression__refcode"])
            progression = course["_CourseProgression__progression"]

            label = ctk.CTkLabel(self.progression_frame, text=f"{course_code['_Courses__title']}\n{progression}%")
            label.pack(side="left", padx=10)

# AllProgression()

