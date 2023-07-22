import tkinter as tk
import customtkinter as ctk

class TodoList:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")

        self.tasks = []
        self.task_var = tk.StringVar()
        self.task_entry = ctk.CTkEntry(master, textvariable=self.task_var,corner_radius=20,width=200,fg_color="white",border_color="Goldenrod3",text_color="Black")
        self.task_entry.pack(pady=(10,0))

        self.add_button = ctk.CTkButton(master, text="Add Task", command=self.add_task,width=20,height=30,corner_radius=20,fg_color="goldenrod3",text_color="black",hover_color="darkgoldenrod2")
        self.add_button.pack(pady=(5,5))

        self.task_frame = ctk.CTkFrame(master,width=200)
        self.task_frame.pack()

        self.delete_button = ctk.CTkButton(master, text="Delete Completed Tasks", command=self.delete_tasks,corner_radius=20,height=30,fg_color="goldenrod3",text_color="black",hover_color="darkgoldenrod2")
        self.delete_button.pack(pady=(5,5))

    def add_task(self):
        task = self.task_var.get()
        if task:
            task_var = tk.StringVar(value=task)
            self.tasks.append((task_var, tk.BooleanVar()))

            task_frame = ctk.CTkFrame(self.task_frame)
            task_frame.pack(side=tk.TOP)

            checkbox = tk.Checkbutton(task_frame, variable=self.tasks[-1][1])
            checkbox.pack(side=tk.LEFT)

            label = ctk.CTkLabel(task_frame, textvariable=task_var,text_color="white")
            label.pack(side=tk.LEFT,padx=10)

            edit_button = ctk.CTkButton(task_frame, text="Edit", command=lambda: self.edit_task(task_var),width=50,height=30,corner_radius=20,fg_color="goldenrod3",text_color="black",hover_color="darkgoldenrod2")
            edit_button.pack(side=tk.LEFT)

            remove_button = ctk.CTkButton(task_frame, text="Remove", command=lambda: self.remove_task(task_var, task_frame),width=50,height=30,corner_radius=20,fg_color="goldenrod3",text_color="black",hover_color="darkgoldenrod2")
            remove_button.pack(side=tk.LEFT)

            self.task_var.set("")

    def edit_task(self, task_var):
        edit_window = ctk.CTkToplevel()
        edit_window.title("Edit Task")
        edit_window.geometry("200x100")

        edit_var = tk.StringVar(value=task_var.get())
        edit_entry = ctk.CTkEntry(edit_window, textvariable=edit_var,corner_radius=20,fg_color="white",border_color="goldenrod3",text_color="black")
        edit_entry.pack(pady=10)

        def update_task():
            new_task = edit_var.get()
            if new_task:
                task_var.set(new_task)
                edit_window.destroy()

        update_button = ctk.CTkButton(edit_window, text="Update", command=update_task,corner_radius=20,fg_color="goldenrod3",text_color="black",hover_color="darkgoldenrod2")
        update_button.pack()

    def remove_task(self, task_var, task_frame):
        for i, (t, _) in enumerate(self.tasks):
            if t == task_var:
                self.tasks.pop(i)
                task_frame.destroy()

    def delete_tasks(self):
        for task_var, checked in self.tasks[:]:
            if checked.get():
                for widget in self.task_frame.winfo_children():
                    if widget.winfo_children()[1].cget("textvariable") == task_var:
                        widget.destroy()
                self.tasks.remove((task_var, checked))

root = ctk.CTk()
root.geometry("500x325")
todo_list = TodoList(root)
root.mainloop()
