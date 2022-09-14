from distutils.cmd import Command
from tkinter import *
import customtkinter as CT
import mysql.connector as m
from tkinter import messagebox


root = CT.CTk()
root.geometry("780x540")
frame = CT.CTkFrame(root, border_width=2, border_color="white")

CT.set_default_color_theme("green")
CT.set_appearance_mode("dark")

def delete_db_win():
    def delete_db():
        try:
            database_entry = delete_db_name_entry.get()
            db = m.connect(host="localhost", user="root", password="toor")
            c = db.cursor()
            c.execute(f"drop database {database_entry};")
            messagebox.showinfo(
                "Database Deleted",
                f"Database {database_entry} has been sucessfully deleted!😎😎😎"
            )

        except:
            messagebox.showerror(
                "Error 404",
                f"Error whild deleteting database {database_entry}!"
            )
        
    delete_db_heading_label = CT.CTkLabel(
        frame, text="DELETE DATABASE", text_font=("Aerial bold", 24)
    ).grid(row=0, column=0, columnspan=3, pady=(30, 20), padx=(10, 10))

    delete_db_subheading_label = CT.CTkLabel(frame, text = "Enter the name of the Database to be deleted", text_font=("aerial",16)).grid(row=1, column=0, columnspan=3, padx=(10, 10), pady=(0, 30))

    delete_db_name = CT.CTkLabel(frame, text = "NAME", text_font= ("aerial",18)).grid(row = 2, column = 0, pady=10, padx=(20, 0))

    delete_db_name_entry = CT.CTkEntry(frame, text_font=("aerial",18), width = 250)
    delete_db_name_entry.grid(row = 2, column = 1, pady=10, padx=(0, 60))

    delete_db_button = CT.CTkButton(frame, text = "Delete Database",text_font=("aerial",18), command = delete_db).grid(row = 3, column = 0, columnspan = 3, pady=(30, 40))

    frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)

delete_db_win()

root.mainloop()