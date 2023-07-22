import tkinter as tk
import customtkinter as ctk
import tkinter.messagebox as msgbox
from datetime import datetime, timedelta

class ReminderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Reminder App")
        self.master.geometry("600x450")
        
        self.reminder_label = ctk.CTkLabel(self.master, text="Set Reminder:", font=("Sans", 20))
        self.reminder_label.pack(pady=(50,0))

        self.hour_slider = ctk.CTkSlider(self.master, from_=1, to=12,number_of_steps=12,width=500,progress_color="Light Blue",command=self.update_hour_entry)
        self.hour_slider.set(1)
        self.hour_slider.pack(pady=10)

        self.hour_entry = ctk.CTkEntry(self.master, font=("Sans", 12), width=28)
        self.hour_entry.insert(0, "01")
        self.hour_entry.pack(pady=10)
        
        self.minute_slider = ctk.CTkSlider(self.master, from_=0, to=59,width=500, number_of_steps=59,progress_color="Light Blue",command=self.update_minute_entry)
        self.minute_slider.set(0)
        self.minute_slider.pack(pady=10)

        self.minute_entry = ctk.CTkEntry(self.master, font=("Sans", 12), width=28)
        self.minute_entry.insert(0, "00")
        self.minute_entry.pack(pady=10)
        
        self.am_pm_var = tk.StringVar()
        self.am_pm_var.set("AM")
        
        self.am_pm_checkbox = ctk.CTkSwitch(self.master, text="PM", variable=self.am_pm_var, onvalue="PM", offvalue="AM", font=("Arial", 12))
        self.am_pm_checkbox.pack(pady=10)
        
        self.set_button = tk.Button(self.master, text="Set", font=("Arial", 16), command=self.set_reminder)
        self.set_button.pack(pady=10)
        
        self.cancel_button = tk.Button(self.master, text="Cancel", font=("Arial", 16), command=self.cancel_reminder)
        self.cancel_button.pack(pady=10)
        
        self.reminder_id = None


    def update_hour_entry(self, value):
        self.hour_entry.delete(0, tk.END)
        self.hour_entry.insert(0, f"{int(value):02d}")
        
    def update_minute_entry(self, value):
        self.minute_entry.delete(0, tk.END)
        self.minute_entry.insert(0, f"{int(value):02d}")

    def set_reminder(self):
        hours = self.hour_slider.get()
        minutes = self.minute_slider.get()
        am_pm = self.am_pm_var.get()
        
        if am_pm == "PM" and hours < 12:
            hours += 12
        elif am_pm == "AM" and hours == 12:
            hours = 0
        
        now = datetime.now()
        reminder_time = datetime(now.year, now.month, now.day, hours, minutes)
        if reminder_time < now:
            reminder_time += timedelta(days=1)
        seconds = (reminder_time - now).total_seconds()
        self.reminder_id = self.master.after(int(seconds * 1000), self.show_reminder)
        
    def show_reminder(self):
        hours = self.hour_slider.get()
        minutes = self.minute_slider.get()
        am_pm = self.am_pm_var.get()
        msgbox.showinfo("Reminder", f"Reminder: {hours:02d}:{minutes:02d} {am_pm}")
        
        self.reminder_id = None
        
    def cancel_reminder(self):
        if self.reminder_id is not None:
            self.master.after_cancel(self.reminder_id)
            self.reminder_id = None
            msgbox.showinfo("Reminder", "Reminder canceled")
        
root = ctk.CTk()
app = ReminderApp(root)
root.mainloop()
