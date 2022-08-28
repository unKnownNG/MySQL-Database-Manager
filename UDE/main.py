from tkinter import *
import customtkinter as CT
import mysql.connector as m


root = CT.CTk()
root.geometry("780x540")
frame = CT.CTkFrame(root, border_width=2, border_color="white")

CT.set_default_color_theme("green")


def create_database_win():

    def create_db():
        database_entry = entry.get()
        db = m.connect(host="localhost", user="root", password="toor")
        c = db.cursor()
        c.execute(f"create database {database_entry};")

    heading_label = CT.CTkLabel(
        frame, text="CREATE DATABASE", text_font=("Arial bold", 22)
    ).grid(row=0, column=0, columnspan=3, pady=(30, 10))

    subheading_label = CT.CTkLabel(
        frame,
        text="Enter the following details to create the database",
        text_font=("Arial", 12),
    ).grid(row=1, column=0, columnspan=3, pady=(0, 30))

    database_name = CT.CTkLabel(frame, text="NAME", text_font=("Arial", 14)).grid(
        row=2, column=0, pady=10, padx=(20, 0)
    )

    entry = CT.CTkEntry(
        frame,
        text_font=("Arial", 16),
        width=250,
    )

    entry.grid(row=2, column=1, pady=10, padx=(0, 60))

    # global database_entry

    create_db_button = CT.CTkButton(
        frame, text="Create Database", command=create_db, text_font=("Arial", 16)
    ).grid(row=3, column=0, columnspan=3, pady=(30, 40))

    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

create_database_win()


root.mainloop()
