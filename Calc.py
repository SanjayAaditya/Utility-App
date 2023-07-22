import tkinter as tk
import customtkinter as ctk
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("440x525")
        self.master.resizable(False, False)

        self.equation = tk.StringVar()
        self.equation.set("")

        self.display = ctk.CTkEntry(self.master, width=420, height=100, font=("Sans Serif", 50), textvariable=self.equation, justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        button_list = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("+", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3),
            ("0", 4, 0), ("00", 4, 1), ("/", 4, 2), ("=", 4, 3)
        ]

        for button in button_list:
            button_text, row, column = button
            button = ctk.CTkButton(self.master, text=button_text, width=90, height=70, font=("Sans Serif", 25), command=lambda x=button_text:self.button_click(x))
            button.grid(row=row, column=column, padx=10, pady=15)

    def button_click(self, text):
        if text == "C":
            self.equation.set("")
        elif text == "=":
            try:
                result = str(eval(self.equation.get()))
                self.equation.set(result)
            except:
                self.equation.set("Error")
        else:
            current_equation = self.equation.get()
            current_equation += text
            self.equation.set(current_equation)

if __name__ == '__main__':
    root = ctk.CTk()
    root.geometry("500x500")
    calculator = Calculator(root)
    root.mainloop()
