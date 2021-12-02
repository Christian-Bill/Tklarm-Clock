import tkinter as tk
from tkinter import ttk
from time import strftime

# Creating tkinter window
root = tk.Tk()
root.title("Relarm Clock")


def current_time_label(root):
    '''Create current time label'''
    time_frame = ttk.Frame(root, style="teststyle.TFrame",)
    time_label = ttk.Label(time_frame, font=("calibri", 35, "bold"), width=14, anchor="center",
                            background="black", foreground="white")
    time_label.pack(side='left', fill='x', expand=True, pady=10)
    time_frame.pack(side='top', fill='x', expand=True)
    show_current_time(time_label)

    # style = ttk.Style()
    # style.configure('TFrame', background="#000")

def show_current_time(time_label):
    """To recursively display time"""
    time_string = strftime('%I:%M:%S %p')
    time_label.config(text=time_string)
    time_label.after(1000, lambda: show_current_time(time_label))

current_time_label(root)

style = ttk.Style()
style.configure("teststyle.TFrame", background="#000")

tk.mainloop()
if __name__ == "__main__":
    pass