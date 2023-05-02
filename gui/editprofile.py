from tkinter import *
from tkinter.font import *
from tkcalendar import DateEntry
import tkinter.messagebox
import customtkinter
import requests
import json

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")


class EditProfile:
    def __init__(self, username, user_type):
        self.__txtcolor = "white"
        self.__username = username
        self.__user_type = user_type

        # --------------------- Create GUI ----------------------- #
        self.__edit_profile = customtkinter.CTkToplevel()
        self.__header_font = customtkinter.CTkFont(family="Kanit", weight="bold", size=20)
        self.__normal_font = customtkinter.CTkFont(family="Kanit", weight="normal", size=16)
        self.__txtbox_font = customtkinter.CTkFont(family="Kanit", weight="normal", size=12)
        self.__edit_profile.title("Edit Profile")
        self.__edit_profile.geometry("400x500")
        self.__edit_profile.resizable(width=False, height=False)

        # Buttons
        customtkinter.CTkButton(self.__edit_profile, text="Save", font=self.__normal_font,
                                command=self.save_profile).pack(side=BOTTOM)
        # Labels
        customtkinter.CTkLabel(self.__edit_profile, text="My Profile", font=self.__header_font).pack(anchor="center")

        customtkinter.CTkLabel(self.__edit_profile, text="Password :", font=self.__normal_font).place(x=80, y=55)
        self.__change_pass = customtkinter.CTkEntry(self.__edit_profile)
        self.__change_pass.place(x=180, y=55)

        customtkinter.CTkLabel(self.__edit_profile, text="Email :", font=self.__normal_font).place(x=80, y=85)
        self.__change_email = customtkinter.CTkEntry(self.__edit_profile)
        self.__change_email.place(x=180, y=85)

        customtkinter.CTkLabel(self.__edit_profile, text="Name :", font=self.__normal_font).place(x=80, y=115)
        self.__change_name = customtkinter.CTkEntry(self.__edit_profile)
        self.__change_name.place(x=180, y=115)

        customtkinter.CTkLabel(self.__edit_profile, text="Surname :", font=self.__normal_font).place(x=80, y=145)
        self.__change_lanme = customtkinter.CTkEntry(self.__edit_profile)
        self.__change_lanme.place(x=180, y=145)

        customtkinter.CTkLabel(self.__edit_profile, text="Gender :", font=self.__normal_font).place(x=80, y=175)
        n = customtkinter.StringVar(value="Male")
        self.__change_gender = customtkinter.CTkComboBox(master=self.__edit_profile, values=["Male", "Female", "Other"], variable=n)
        self.__change_gender.place(x=180, y=175)

        customtkinter.CTkLabel(self.__edit_profile, text="BirthDate :", font=self.__normal_font).place(x=80, y=205)
        self.__change_birthdate = DateEntry(self.__edit_profile, width=25,background="blue", foreground="sky-blue", bd=4)
        self.__change_birthdate.place(x=225, y=265)

        customtkinter.CTkLabel(self.__edit_profile, text="Education :", font=self.__normal_font).place(x=80, y=235)
        self.__change_educate = customtkinter.CTkEntry(self.__edit_profile)
        self.__change_educate.place(x=180, y=235)

        customtkinter.CTkLabel(self.__edit_profile, text="Province :", font=self.__normal_font).place(x=80, y=265)
        self.__change_province = customtkinter.CTkEntry(self.__edit_profile)
        self.__change_province.place(x=180, y=265)

        customtkinter.CTkLabel(self.__edit_profile, text="Country :", font=self.__normal_font).place(x=80, y=295)
        self.__change_country = customtkinter.CTkEntry(self.__edit_profile)
        self.__change_country.place(x=180, y=295)

        if self.__user_type == "Teacher":
            customtkinter.CTkLabel(self.__edit_profile, text="Department :", font=self.__normal_font).place(x=80, y=325)
            self.__change_dept = customtkinter.CTkEntry(self.__edit_profile)
            self.__change_dept.place(x=180, y=325)

    def save_profile(self):
        pass
