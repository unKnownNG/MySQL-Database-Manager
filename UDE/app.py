import customtkinter as CT
from tkinter import *
import mysql.connector as m
from tkinter import messagebox
from PIL import Image, ImageTk
import time

CT.set_default_color_theme(
    "D:\\Programing\\Projects\\Ultimate Database Manager 2\\UDE\\theme.json"
)


class App(CT.CTk):
    def __init__(self):
        super().__init__()
        self.ButtonFont = "Aerial"
        self.navBarFont = "monospace", 20

        imgBg = Image.open(
            "D:\Programing\\Projects\\Ultimate Database Manager 2\\UDE\\img\\image.jpg"
        )
        self.bg_image = ImageTk.PhotoImage(imgBg)
        imageBackBtn = Image.open(
            "D:\\Programing\\Projects\\Ultimate Database Manager 2\\UDE\\img\\back.PNG"
        ).resize((30, 30))
        self.photoBackBtn = ImageTk.PhotoImage(imageBackBtn)

        self.bg = CT.CTkLabel(image=self.bg_image).place(
            relx=0.5, rely=0.5, anchor=CENTER
        )

        self.loginWindow()

    @classmethod
    def back(self, currentFrm, destinedFrm):
        currentFrm.destroy()

    def alterTable(self):
        self.tableHomeFrame.destroy()
        self.alterTableFrm = CT.CTkFrame(self)

    def progress(self):
        self.progressBar.set(0.2)
        self.update_idletasks()
        time.sleep(1)
        self.progressBar.set(0.4)
        self.update_idletasks()
        time.sleep(1)
        self.progressBar.set(0.6)
        self.update_idletasks()
        time.sleep(1)
        self.progressBar.set(0.8)
        self.update_idletasks()
        time.sleep(1)
        self.progressBar.set(1)

    def sliderFun(self):
        self.sliderFrm = CT.CTkFrame(self)
        self.progressBar = CT.CTkProgressBar(self.sliderFrm, height=20, width=400)
        self.progressBar.grid(row=1, column=0, padx=200, pady=(30))
        self.progressBar.set(0)

        queryLabel = CT.CTkLabel(
            self.sliderFrm, text="QUERY  I N  PROCESS", text_font=("Anurati", 28)
        ).grid(row=0, column=0, columnspan=3, pady=(90, 60), padx=(10, 10))

        backBtn = CT.CTkButton(
            self.sliderFrm,
            text="HOME",
            height=30,
            width=30,
            text_font=("Anurati", 18),
            command=lambda: self.back(self.sliderFrm, self.homeWindow()),
        ).grid(row=3, column=0, columnspan=3, pady=(50, 80))

        self.sliderFrm.place(relx=0.5, rely=0.5, anchor=CENTER)

    def deleteTableFun(self):
        try:
            dataBase = self.delTableComboobx.get()
            self.cur.execute(f"use {dataBase};")
            table = self.deleteTableEntry.get()
            self.cur.execute(f"drop table {table};")
            self.deleteTableFrm.destroy()
            self.sliderFun()
            self.progress()
            messagebox.showinfo(
                "Table Deleted Sucessfully",
                f"Table {table} has been sucessfully deleted",
            )

        except:
            messagebox.showerror("Error !U2*61234", "Please chech you input")

    def deleteTable(self):
        self.tableHomeFrame.destroy()
        self.deleteTableFrm = CT.CTkFrame(self)

        delTableHeading = CT.CTkLabel(
            self.deleteTableFrm, text="D E L E T E  TA B L E", text_font=("Anurati", 28)
        ).grid(row=0, column=0, columnspan=3, pady=(30, 20), padx=(10, 10))

        delTableSubHeading = CT.CTkLabel(
            self.deleteTableFrm,
            text="Enter the following details to delete the Table",
            text_font=("Arial", 12),
        ).grid(row=1, column=0, columnspan=3, pady=(0, 30))

        selectDB = CT.CTkLabel(
            self.deleteTableFrm, text="DATABASE", text_font=("anurati", 18)
        ).grid(row=2, column=0, pady=(20), padx=(60, 0))

        dataBaseList = []
        self.cur.execute("show databases;")
        a = self.cur.fetchall()

        for i in a:
            dataBaseList.append(str(i))

        self.delTableComboobx = CT.CTkComboBox(
            self.deleteTableFrm, values=dataBaseList, height=30, width=250
        )
        self.delTableComboobx.grid(row=2, column=1, pady=(20), padx=(20, 40))
        self.delTableComboobx.set("Select DataBase")

        delTableLab = CT.CTkLabel(
            self.deleteTableFrm, text="NAME", text_font=("anurati", 18)
        ).grid(row=3, column=0, pady=10, padx=(20, 20))

        self.deleteTableEntry = CT.CTkEntry(
            self.deleteTableFrm, text_font=("Arial", 16), width=250, corner_radius=20
        )

        self.deleteTableEntry.grid(row=3, column=1, pady=10, padx=(30, 60))

        delTableButton = CT.CTkButton(
            self.deleteTableFrm,
            text="Delete Table",
            command=self.deleteTableFun,
            text_font=("Arial", 16),
        ).grid(row=4, column=0, columnspan=3, pady=(30, 40))

        backBtn = CT.CTkButton(
            self.deleteTableFrm,
            text="",
            fg_color="#171520",
            height=30,
            width=30,
            image=self.photoBackBtn,
            text_font=("aerial", 18),
            command=lambda: self.back(self.deleteTableFrm, self.tableHomeWin()),
        ).place(x=0, y=0)

        self.deleteTableFrm.place(relx=0.5, rely=0.5, anchor=CENTER)

    def tableHomeWin(self):
        self.navBarDestroy()
        self.tableHomeFrame = CT.CTkFrame(self)

        createTableBtn = CT.CTkButton(
            self.tableHomeFrame, text="Create Table", text_font=(self.ButtonFont, 20)
        ).grid(row=0, column=0, columnspan=3, pady=(60, 40), padx=80)

        alterTableBtn = CT.CTkButton(
            self.tableHomeFrame, text="Alter Table", text_font=(self.ButtonFont, 20)
        ).grid(row=1, column=0, columnspan=3, pady=40, padx=80)

        deleteTableBtn = CT.CTkButton(
            self.tableHomeFrame,
            text="Delete Table",
            text_font=(self.ButtonFont, 20),
            command=self.deleteTable,
        ).grid(row=2, column=0, columnspan=3, padx=80, pady=(40, 60))

        backBtn = CT.CTkButton(
            self.tableHomeFrame,
            text="",
            fg_color="#171520",
            height=30,
            width=30,
            image=self.photoBackBtn,
            text_font=("aerial", 18),
            command=lambda: self.back(self.tableHomeFrame, self.homeWindow()),
        ).place(x=0, y=0)

        self.tableHomeFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

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
                f"Database {databaseEntry} has been sucessfully deleted!😎😎😎",
            )

        except:
            messagebox.showerror(
                "Error 404", f"Error while deleteting database {databaseEntry}!"
            )

    def createDataBaseWin(self):
        global createDBEntry

        self.dataBaseOptionFrame.destroy()
        self.createDBWin = CT.CTkFrame(self)

        create_db_heading_label = CT.CTkLabel(
            self.createDBWin,
            text="C R E A T E  DA T A B A S E",
            text_font=("Anurati", 24),
        ).grid(row=0, column=0, columnspan=3, pady=(30, 20), padx=(10, 10))

        create_db_subheading_label = CT.CTkLabel(
            self.createDBWin,
            text="Enter the following details to create the database",
            text_font=("Arial", 12),
        ).grid(row=1, column=0, columnspan=3, pady=(0, 30))

        create_db_database_name = CT.CTkLabel(
            self.createDBWin, text="NAME", text_font=("anurati", 18)
        ).grid(row=2, column=0, pady=10, padx=(20, 0))

        createDBEntry = CT.CTkEntry(
            self.createDBWin, text_font=("Arial", 16), width=250, corner_radius=20
        )

        createDBEntry.grid(row=2, column=1, pady=10, padx=(0, 60))

        create_db_button = CT.CTkButton(
            self.createDBWin,
            text="Create Database",
            command=self.createDataBaseFun,
            text_font=("Arial", 16),
        ).grid(row=3, column=0, columnspan=3, pady=(30, 40))

        backBtn = CT.CTkButton(
            self.createDBWin,
            text="",
            fg_color="#171520",
            height=30,
            width=30,
            image=self.photoBackBtn,
            text_font=("aerial", 18),
            command=lambda: self.back(self.createDBWin, self.dataBaseWindow()),
        ).place(x=0, y=0)
        self.createDBWin.place(relx=0.5, rely=0.5, anchor=CENTER)

    def alterDataBaseWin(self):
        self.dataBaseOptionFrame.destroy()
        self.alterDBFrame = CT.CTkFrame(self)

        createTableBtn = CT.CTkButton(
            self.alterDBFrame, text="Create Table", text_font=(self.ButtonFont, 20)
        ).grid(row=0, column=0, columnspan=3, pady=(60, 40), padx=80)

        alterTableBtn = CT.CTkButton(
            self.alterDBFrame, text="Alter Table", text_font=(self.ButtonFont, 20)
        ).grid(row=1, column=0, columnspan=3, pady=40, padx=80)

        deleteTableBtn = CT.CTkButton(
            self.alterDBFrame, text="Delete Table", text_font=(self.ButtonFont, 20)
        ).grid(row=2, column=0, columnspan=3, padx=80, pady=(40, 60))

        backBtn = CT.CTkButton(
            self.alterDBFrame,
            text="",
            fg_color="#171520",
            height=30,
            width=30,
            image=self.photoBackBtn,
            text_font=("aerial", 18),
            command=lambda: self.back(self.alterDBFrame, self.dataBaseWindow()),
        ).place(x=0, y=0)

        self.alterDBFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

    def deleteDataBaseWin(self):
        global deleteDBEntry

        # self.dataBaseOptionFrame.destroy()
        self.deleteDBFrame = CT.CTkFrame(self)

        delete_db_heading_label = CT.CTkLabel(
            self.deleteDBFrame,
            text="D E L E T E D A T A B A S E",
            text_font=("Anurati", 26),
        ).grid(row=0, column=0, columnspan=3, pady=(60, 20), padx=(60, 60))

        delete_db_subheading_label = CT.CTkLabel(
            self.deleteDBFrame,
            text="Enter the name of the Database to be deleted",
            text_font=("aerial", 16),
        ).grid(row=1, column=0, columnspan=3, padx=(10, 10), pady=(20, 30))

        delete_db_name = CT.CTkLabel(
            self.deleteDBFrame, text="NAME", text_font=("Anurati", 22)
        ).grid(row=2, column=0, pady=30, padx=(20, 0))

        deleteDBEntry = CT.CTkEntry(
            self.deleteDBFrame, text_font=("aerial", 20), width=290, corner_radius=20
        )
        deleteDBEntry.grid(row=2, column=1, pady=30, padx=(0, 40))

        delete_db_button = CT.CTkButton(
            self.deleteDBFrame,
            text="Delete Database",
            text_font=("aerial", 20),
            corner_radius=15,
            command=self.deleteDataBaseFun,
        ).grid(row=3, column=0, columnspan=3, pady=(30, 60))

        backBtn = CT.CTkButton(
            self.deleteDBFrame,
            text="",
            fg_color="#171520",
            height=30,
            width=30,
            image=self.photoBackBtn,
            command=lambda: self.back(self.deleteDBFrame, self.dataBaseWindow()),
        ).place(x=0, y=0)
        self.deleteDBFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

    def dataBaseWindow(self):
        self.dataBaseOptionFrame = CT.CTkFrame(self)
        self.navBarDestroy()

        createDataBaseBtn = CT.CTkButton(
            self.dataBaseOptionFrame,
            text="Create Database",
            text_font=(self.ButtonFont, 20),
            command=self.createDataBaseWin,
        ).grid(row=0, column=0, columnspan=3, pady=(60, 40), padx=80)

        alterDataBaseBtn = CT.CTkButton(
            self.dataBaseOptionFrame,
            text="Alter Database",
            text_font=(self.ButtonFont, 20),
            command=self.alterDataBaseWin,
        ).grid(row=1, column=0, columnspan=3, pady=40, padx=80)

        deleteDataBaseBtn = CT.CTkButton(
            self.dataBaseOptionFrame,
            text="Delete Database",
            text_font=(self.ButtonFont, 20),
            command=self.deleteDataBaseWin,
        ).grid(row=2, column=0, columnspan=3, padx=80, pady=(40, 60))

        backBtn = CT.CTkButton(
            self.dataBaseOptionFrame,
            text="",
            fg_color="#171520",
            height=30,
            width=30,
            image=self.photoBackBtn,
            text_font=("aerial", 18),
            command=lambda: self.back(self.dataBaseOptionFrame, self.homeWindow()),
        ).place(x=0, y=0)

        self.dataBaseOptionFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

    def login(self):
        global mysql_con

        login_user = login_name_entry.get()
        login_password = login_passwrd_entry.get()

        try:
            mysql_con = m.connect(
                user=login_user, host="localhost", password=login_password
            )
            self.cur = mysql_con.cursor()
            messagebox.showinfo(
                "Sucessfully connected", "You have logged into mysql server"
            )
            self.loginFrame.destroy()
            self.homeWindow()

        except:
            messagebox.showerror("Error", "Please check your input")

    def homeWindow(self):
        self.navBar()

    def navBarDestroy(self):
        self.homeBtn.destroy()
        self.dbBtn.destroy()
        self.tableBtn.destroy()
        self.loginBtn.destroy()

    def navBar(self):

        self.homeBtn = CT.CTkButton(
            self,
            text="HOME",
            height=60,
            text_font=("anurati", 16),
            hover_color="#41ead4",
            corner_radius=0,
        )
        self.homeBtn.grid(row=0, column=0)

        self.dbBtn = CT.CTkButton(
            self,
            text="DATABASE",
            height=60,
            width=180,
            hover_color="#ff006e",
            text_font=("anurati", 16),
            corner_radius=0,
            command=self.dataBaseWindow,
        )
        self.dbBtn.grid(row=0, column=1)

        self.tableBtn = CT.CTkButton(
            self,
            text="TABLE",
            height=60,
            hover_color="#ffd60a",
            text_font=("anurati", 16),
            corner_radius=0,
            command=self.tableHomeWin,
        )
        self.tableBtn.grid(row=0, column=2)

        self.loginBtn = CT.CTkButton(
            self,
            text="DEVELOPERS",
            height=60,
            width=180,
            text_font=("anurati", 16),
            hover_color="#ef233c",
            corner_radius=0,
        )
        self.loginBtn.grid(row=0, column=3)

    def loginWindow(self):
        global login_name_entry, login_passwrd_entry

        self.loginFrame = CT.CTkFrame(self, image=self.bg)
        login_heading_label = CT.CTkLabel(
            self.loginFrame, text="S I G N  I N", text_font=("Anurati", 28)
        ).grid(row=0, column=0, columnspan=3, pady=(30, 40), padx=(10, 10))
        login_name_label = CT.CTkLabel(
            self.loginFrame, text="NAME", text_font=("Anurati", 20)
        ).grid(row=1, column=0, pady=(0, 30))
        login_name_entry = CT.CTkEntry(
            self.loginFrame, text_font=("Anurati", 20), width=250, corner_radius=20
        )
        login_name_entry.grid(row=1, column=1, pady=(0, 30), padx=(0, 30))
        login_passwrd_label = CT.CTkLabel(
            self.loginFrame, text="PASSWORD", text_font=("Anurati", 20)
        ).grid(row=2, column=0, padx=(30, 20), pady=(20, 20))
        login_passwrd_entry = CT.CTkEntry(
            self.loginFrame, text_font=("Anurati", 20), width=250, corner_radius=20
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
