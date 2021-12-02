import tkinter as tk
from tkinter import ttk
from time import strftime

# Creating tkinter window
root = tk.Tk()
root.title("Relarm Clock")


def current_time_label():
    '''Create current time label'''
    time_label = ttk.Label(root, font=("calibri", 35, "bold"), width=14, anchor="center",
                            background="black", foreground="white")
    time_label.pack(side='left', fill='x', expand=True, pady=10)
    show_current_time(time_label)

def show_current_time(time_label):
    """To recursively display time"""
    time_string = strftime('%I:%M:%S %p')
    time_label.config(text=time_string)
    time_label.after(1000, lambda: show_current_time(time_label))

if __name__ == "__main__":
    current_time_label()
    tk.mainloop()