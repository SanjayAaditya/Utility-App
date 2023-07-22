import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk

class NoteTaker:
    def __init__(self, master):
        self.master = master
        self.master.title("Note Taker")
        self.master.geometry("300x120")
        
        self.subject_label = ctk.CTkLabel(self.master, text="Enter Subject Below")
        self.subject_label.pack(padx=10, pady=(10,0))
        
        self.subject_entry = ctk.CTkEntry(self.master,fg_color="White",text_color="Black",corner_radius=20)
        self.subject_entry.pack(padx=10)
        
        self.create_button = ctk.CTkButton(self.master, text="Create", command=self.create_panel,fg_color="Green",hover_color="Dark Green",corner_radius=20)
        self.create_button.pack(padx=10, pady=5)

    def create_panel(self):
        subject = self.subject_entry.get()
        self.subject_entry.delete(0, tk.END,)
        panel = ctk.CTkToplevel(self.master)
        panel.title(f"{subject} Notes")
        panel.geometry("600x700")
        
        self.notes_text = tk.Text(panel,font="sans")
        self.notes_text.pack(expand=True, fill=tk.BOTH)
        
        button_frame = ctk.CTkFrame(panel)
        button_frame.pack(side=tk.BOTTOM, pady=10)
        
        save_button = ctk.CTkButton(button_frame, text="Save", command=self.save_notes,corner_radius=20)
        save_button.pack(side=tk.LEFT, padx=10)
        
        load_button = ctk.CTkButton(button_frame, text="Load", command=self.load_notes,corner_radius=20)
        load_button.pack(side=tk.RIGHT, padx=10)
    
    def save_notes(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w") as f:
                f.write(self.notes_text.get("1.0", tk.END))
    
    def load_notes(self):
        file_path = filedialog.askopenfilename(filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        if file_path:
            with open(file_path, "r") as f:
                notes = f.read()
                self.notes_text.delete("1.0", tk.END)
                self.notes_text.insert("1.0", notes)

root = ctk.CTk()
note_taker = NoteTaker(root)
root.mainloop()
