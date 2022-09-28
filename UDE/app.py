import customtkinter as CT
from tkinter import *
import mysql.connector as m
from tkinter import messagebox
import appFuntion as AF


class App( AF.AppFunction):
    def __init__(self):
        super().__init__()
        self.ButtonFont = "Aerial"
        self.loginWindow()

    def createDataBaseFun(self):
        databaseEntry = createDBEntry.get()
        try:
            cur = mysql_con.cursor()
            cur.execute(f"create database {databaseEntry};")
            messagebox.showinfo(
                "Database Created",
                f"Database {databaseEntry} has been successfuly created!",
            )

        except:
            messagebox.showerror(
                "Invalid Input",
                f"Database {databaseEntry} cannot be created. {databaseEntry} database already exists or check your input",
            )

    def deleteDataBaseFun(slef):

        try:
            databaseEntry = deleteDBEntry.get()
            db = m.connect(host="localhost", user="root", password="toor")
            c = db.cursor()
            c.execute(f"drop database {databaseEntry};")
            messagebox.showinfo(
                "Database Deleted",
                f"Database {databaseEntry} has been sucessfully deleted!😎😎😎"
            )

        except:
            messagebox.showerror(
                "Error 404",
                f"Error whild deleteting database {databaseEntry}!"
            )

    def createDataBaseWin(self):
        global createDBEntry

        self.homeFrame.destroy()
        self.createDBWin = CT.CTkFrame(self)

        create_db_heading_label = CT.CTkLabel(
        self.createDBWin, text="C R E A T E  DA T A B A S E", text_font=("Anurati", 24)
        ).grid(row=0, column=0, columnspan=3, pady=(30, 20), padx=(10, 10))

        create_db_subheading_label = CT.CTkLabel(
            self.createDBWin,
            text="Enter the following details to create the database",
            text_font=("Arial", 12),
        ).grid(row=1, column=0, columnspan=3, pady=(0, 30))

        create_db_database_name = CT.CTkLabel(self.createDBWin, text="NAME", text_font=("anurati", 18)).grid(
            row=2, column=0, pady=10, padx=(20, 0)
        )

        createDBEntry = CT.CTkEntry(
            self.createDBWin,
            text_font=("Arial", 16),
            width=250,
        )

        createDBEntry.grid(row=2, column=1, pady=10, padx=(0, 60))

        create_db_button = CT.CTkButton(
            self.createDBWin, text="Create Database", command= self.createDataBaseFun, text_font=("Arial", 16)
        ).grid(row=3, column=0, columnspan=3, pady=(30, 40))

        self.createDBWin.place(relx=0.5, rely=0.5, anchor=CENTER)

    def deleteDataBaseWin(self):
        global deleteDBEntry

        self.homeFrame.destroy()
        self.deleteDBFrame = CT.CTkFrame(self) 

        delete_db_heading_label = CT.CTkLabel(
        self.deleteDBFrame, text="DELETE DATABASE", text_font=("Aerial bold", 24)
        ).grid(row=0, column=0, columnspan=3, pady=(30, 20), padx=(10, 10))

        delete_db_subheading_label = CT.CTkLabel(self.deleteDBFrame, text = "Enter the name of the Database to be deleted", text_font=("aerial",16)).grid(row=1, column=0, columnspan=3, padx=(10, 10), pady=(0, 30))

        delete_db_name = CT.CTkLabel(self.deleteDBFrame, text = "NAME", text_font= ("aerial",18)).grid(row = 2, column = 0, pady=10, padx=(20, 0))

        deleteDBEntry = CT.CTkEntry(self.deleteDBFrame, text_font=("aerial",18), width = 250)
        deleteDBEntry.grid(row = 2, column = 1, pady=10, padx=(0, 60))

        delete_db_button = CT.CTkButton(self.deleteDBFrame, text = "Delete Database",text_font=("aerial",18), command = self.deleteDataBaseFun).grid(row = 3, column = 0, columnspan = 3, pady=(30, 40))

        self.deleteDBFrame.place(relx = 0.5, rely = 0.5, anchor = CENTER)


    def homeWindow(self):
        self.homeFrame = CT.CTkFrame(self)

        createDataBaseBtn = CT.CTkButton(self.homeFrame, text = "Create Database", text_font= (self.ButtonFont,20), command = self.createDataBaseWin).grid(row = 0, column = 0, columnspan = 3, pady = (60, 40), padx = 80)

        alterDataBaseBtn = CT.CTkButton(self.homeFrame, text = "Alter Database", text_font=(self.ButtonFont, 20)).grid(row = 1, column = 0, columnspan = 3, pady = 40, padx = 80)

        deleteDataBaseBtn = CT.CTkButton(self.homeFrame, text = "Delete Database", text_font=(self.ButtonFont, 20), command= self.deleteDataBaseWin).grid(row = 2, column = 0, columnspan = 3, padx = 80, pady = (40,60))

        self.homeFrame.place(relx = 0.5, rely = 0.5, anchor = CENTER)

    def login(self):
        global mysql_con

        login_user = login_name_entry.get()
        login_password = login_passwrd_entry.get()

        try:
            mysql_con = m.connect(
                user=login_user, host="localhost", password=login_password
            )
            messagebox.showinfo(
                "Sucessfully connected", "You have logged into mysql server"
            )
            self.loginFrame.destroy()
            self.homeWindow()

        except:
            messagebox.showerror("Error", "Please check your input")

    def loginWindow(self):
        global login_name_entry, login_passwrd_entry

        self.loginFrame = CT.CTkFrame(self)
        login_heading_label = CT.CTkLabel(
            self.loginFrame, text="S I G N  I N", text_font=("Anurati", 28)
        ).grid(row=0, column=0, columnspan=3, pady=(30, 40), padx=(10, 10))
        login_name_label = CT.CTkLabel(
            self.loginFrame, text="NAME", text_font=("Anurati", 20)
        ).grid(row=1, column=0, pady=(0, 30))
        login_name_entry = CT.CTkEntry(
            self.loginFrame, text_font=("Anurati", 20), width=250
        )
        login_name_entry.grid(row=1, column=1, pady=(0, 30), padx=(0, 30))
        login_passwrd_label = CT.CTkLabel(
            self.loginFrame, text="PASSWORD", text_font=("Anurati", 20)
        ).grid(row=2, column=0, padx=(30, 20), pady=(20, 20))
        login_passwrd_entry = CT.CTkEntry(
            self.loginFrame, text_font=("Anurati", 20), width=250
        )
        login_passwrd_entry.grid(row=2, column=1, padx=(0, 30))
        login_button = CT.CTkButton(
            self.loginFrame,
            text="LOGIN",
            text_font=("arial bold", 20),
            command=self.login,
        ).grid(row=3, column=0, columnspan=3, pady=(40, 20))
        self.loginFrame.place(relx=0.5, rely=0.5, anchor=CENTER)


a = App()
a.mainloop()
