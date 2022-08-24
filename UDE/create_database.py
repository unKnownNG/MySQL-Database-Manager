from tkinter import *



font_family = "Arial"
main_colour = "#3c096c"
gradient_colour = ""
text_colour =  ""
font_size = "20"

root = Tk()
root.geometry("720x540")
root.config(bg= main_colour)

frame = Frame(root, bg = main_colour)


heading = Label(frame, text = "DATABASE FORM", bg= main_colour,font= ("Arial Bold", 24))\
    .grid(row = 0, column = 0, columnspan=3, pady = (0,50))

name = Label(frame, text="Database Name", bg = main_colour, font = (font_family, font_size))\
    .grid(row = 1, column = 0 )

Entry(frame, font = (font_family, font_size)).grid(row = 1, column = 1, padx = (30,0))

create_button = Button(frame, text = "CREATE DATABASE", font= ("Arial bold", 16), bg = "#4cc9f0")\
    .grid(row = 2, column = 0, columnspan = 3, pady = (60,0))


frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)
root.mainloop()