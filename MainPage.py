import tkinter as tk
import customtkinter as ctk
import os

root = ctk.CTk()

root.title("Home Page")

root.geometry("620x363")

def open_program_1():
    os.system("Calc.py")

def open_program_2():
    os.system("NoteTaking.py")

def open_program_3():
    os.system("Todo.py")

def open_program_4():
    os.system("Alarm.py")

button_1 = tk.Button(root, text="Calculator", width=40, height=10, bg="orange", command=open_program_1)
button_2 = tk.Button(root, text="Take Notes", width=40, height=10, bg="light green",command=open_program_2)
button_3 = tk.Button(root, text="Create a To Do List", width=40, height=10, bg="gold",command=open_program_3)
button_4 = tk.Button(root, text="Set a Remainder", width=40, height=10, bg="sky blue",command=open_program_4)

button_1.grid(row=0, column=0, padx=10, pady=10)
button_2.grid(row=0, column=1, padx=10, pady=10)
button_3.grid(row=1, column=0, padx=10, pady=10)
button_4.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()
