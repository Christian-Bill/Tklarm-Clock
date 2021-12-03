# Views for the main app
import tkinter as tk
from controls import *
from tkinter import ttk


class View():
    '''Visual components of the app'''

    def __init__(self):

        self.main_window()
    
    def main_window(self):
        self.root = tk.Tk()
        self.app_components()
        tk.mainloop()

    def app_components(self):
        self.root.title("Tklarm Clock")
        self.widgets()
        self.styles()

    def widgets(self):
        self.current_time_label()
        self.add_delete_btns()

    def current_time_label(self):
        '''Create current time label'''
        self.time_frame = ttk.Frame(self.root, style="time.TFrame",)
        self.create_time_label()
        self.time_frame.pack(side='top', fill='x', expand=True)

    def create_time_label(self):
        time_label = ttk.Label(self.time_frame, font=("calibri", 35, "bold"),
                            width=14, anchor="center", background="black",
                            foreground="white")
        time_label.pack(side='left', fill='x', expand=True, pady=10)
        fetch_current_time(time_label)

    def add_delete_btns(self):
        '''Create Add and Delete labels'''
        self.btns_frame = ttk.Frame(self.root, style="btn.TFrame",)
        self.display_buttons()
        self.btns_frame.pack(side='top', fill='x', expand=True)

    def display_buttons(self):
        self.create_add_button()
        self.create_del_button()

    def create_add_button(self):
        add_btn = ttk.Button(self.btns_frame, text='+', style="btn.TButton")
        add_btn.pack(side='left', fill='x', expand=True)

    def create_del_button(self):
        del_btn = ttk.Button(self.btns_frame, text='-', style="btn.TButton")
        del_btn.pack(side='left', fill='x', expand=True)

    def schedules(self):
        pass

    def styles(self):
        self.style = ttk.Style()
        self.style.configure("time.TFrame", background="#000")


if __name__ == '__main__':
    View()