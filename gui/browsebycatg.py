import requests
import customtkinter as ctk
from gui.coursedetailgui import CourseDetail

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class BrowseCatg:
    def __init__(self,category, username, user_type):
        self.__category = category
        self.__username = username
        self.__user_type = user_type
        self.__root = ctk.CTkToplevel()
        self.__root.title("Course Categories")
        self.__title_font = ctk.CTkFont(family="Kanit", weight="bold", size=30)
        self.__header_font = ctk.CTkFont(family="Kanit", weight="bold", size=20)
        self.__normal_font = ctk.CTkFont(family="Kanit", weight="normal", size=15)
        self.__root.geometry("600x400")
        self.create_course_list_window(self.__category)       
        # self.__root.resizable(width=False, height=False)
        self.__root.mainloop()
     
    def browse_courses(self, category):
        url = f"http://127.0.0.1:8000/courses/category/{category}"
        response = requests.get(url)
        return response.json()
    
    def on_button_click(course_refcode):
        return course_refcode
            
    def create_course_list_window(self, category):
        courses = self.browse_courses(category)
        max_courses_per_row = 3
        window_width = 600
        
        self.courses_label = ctk.CTkLabel(self.__root, text=f'Category : "{category}"', font=self.__title_font)
        self.courses_label.pack(side=ctk.TOP, padx=10, pady=10)

        course_rows = []
        row_frame = ctk.CTkFrame(self.__root, width=window_width)
        row_frame.pack(side=ctk.TOP, padx=10, pady=5, fill=ctk.X)
        course_rows.append(row_frame)

        for index, course in enumerate(courses):
            if index % max_courses_per_row == 0 and index != 0:
                row_frame = ctk.CTkFrame(self.__root, width=window_width)
                row_frame.pack(side=ctk.TOP, padx=10, pady=5, fill=ctk.X)
                course_rows.append(row_frame)

            course_frame = ctk.CTkFrame(row_frame)
            course_frame.pack(side=ctk.LEFT, padx=10, pady=5, expand=True)

            refcode_label = ctk.CTkLabel(course_frame, text=course["_Courses__refcode"], font=self.__header_font).pack()
            title_label = ctk.CTkLabel(course_frame, text=course["_Courses__title"], font=self.__header_font).pack()
            button = ctk.CTkButton(course_frame,
                                text="Detail",
                                command=lambda course_refcode=course["_Courses__refcode"]: self.detail(course_refcode))
            button.pack()
            
    def detail(self, ref):
        CourseDetail(self.__username, ref, self.__user_type)
        
# BrowseCatg("Math","ffwatcharin","Student")
