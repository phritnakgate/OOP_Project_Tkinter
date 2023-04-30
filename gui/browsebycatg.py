import customtkinter
from tkinter import *
from tkinter.font import *
import tkinter.messagebox
import requests
import json
from functools import partial

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

class BrowseByCatg:
    def __init__(self, catg):
        self.__catg = catg
        self.__browsebycatg = customtkinter.CTkToplevel()
        self.__header_font = customtkinter.CTkFont(family="Kanit", weight="bold", size=20)
        self.__normal_font = customtkinter.CTkFont(family="Kanit", weight="normal", size=16)
        self.__txtbox_font = customtkinter.CTkFont(family="Kanit", weight="normal", size=12)
        self.__browsebycatg.title("Browse by" + self.__catg)
        self.__browsebycatg.geometry("700x700")
        self.__browsebycatg.resizable(width=False, height=False)
        customtkinter.CTkLabel(self.__browsebycatg ,text=self.__catg + ' courses', font=self.__header_font).pack(anchor='center')

        self.__browsebycatg.mainloop()
        
BrowseByCatg(' Math')        