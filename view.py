import tkinter as tk
from controls import *
from tkinter import ttk


class View():
    '''Visual components of Tklarm Clock'''

    def __init__(self):

        self.main_window()
    
    def main_window(self):
        self.root = tk.Tk()
        self.window_size()
        self.app_components()
        tk.mainloop()

    def window_size(self):
        self.root.geometry('426x562')
        self.root.resizable(0, 0)

    def app_components(self):
        self.root.title("Tklarm Clock")
        self.widgets()
        self.styles()

    def widgets(self):
        self.current_time_label()
        self.hour_event_entries()
        self.add_delete_btns()
        self.schedules()

    def current_time_label(self):
        '''Create Current Time Label'''
        self.time_frame = ttk.Frame(self.root, style="time.TFrame")
        self.create_time_label()
        self.time_frame.pack(side='top', fill='both')

    def create_time_label(self):
        time_label = ttk.Label(self.time_frame, font=("calibri", 35, "bold"),
                            anchor="center", background="black",
                            foreground="white")
        time_label.pack(side='top', fill='both', expand=True, pady=10)
        fetch_current_time(time_label)

    def hour_event_entries(self):
        '''Create Hour and Event Entries'''
        self.entry_frame = ttk.Frame(self.root, height='5', style="entries.TFrame")
        self.create_hour_entry()
        self.create_event_entry()     
        self.entry_frame.pack(side='top', fill='both')

    def create_hour_entry(self):
        self.hour_labelframe = ttk.LabelFrame(self.entry_frame, text='Hour', style="hour.TLabelframe")
        search_entry = ttk.Entry(self.hour_labelframe)
        search_entry.pack(side='left', fill='both', expand=True, pady=5, padx=5)
        self.hour_labelframe.pack(side='left', fill='both', expand=True, pady=5, padx=5)

    def create_event_entry(self):
        self.event_frame = ttk.LabelFrame(self.entry_frame, text='Event', style="event.TLabelframe")
        event_entry = ttk.Entry(self.event_frame)
        event_entry.pack(side='left', fill='both', expand=True, pady=5, padx=5)
        self.event_frame.pack(side='left', fill='both', expand=True, pady=5, padx=5)

    def add_delete_btns(self):
        '''Create Add and Delete Buttons'''
        self.btns_frame = ttk.Frame(self.root, height='5', style="entries.TFrame")
        self.create_btn_labelframe()
        self.btns_frame.pack(side='top', fill='both')

    def create_btn_labelframe(self):
        self.btns_labelframe = ttk.LabelFrame(self.btns_frame, text='Controls', style="btn.TLabelframe")
        self.display_buttons()
        self.btns_labelframe.pack(side='top', fill='both', expand=True, pady=5, padx=5)

    def display_buttons(self):
        self.create_add_button()
        self.create_del_button()

    def create_add_button(self):
        add_btn = ttk.Button(self.btns_labelframe, text='+', style="btn.TButton")
        add_btn.pack(side='left', fill='both', expand=True, pady=5, padx=5)

    def create_del_button(self):
        del_btn = ttk.Button(self.btns_labelframe, text='-', style="btn.TButton")
        del_btn.pack(side='left', fill='both', expand=True, pady=5, padx=5)

    def schedules(self):
        '''Create Schedules Treeview'''
        self.sched_frame = ttk.Frame(self.root, style="sched.TFrame")
        self.create_sched_labelframe()
        self.sched_frame.pack(side='bottom', fill='both', expand=True)
        self.sched_tree.bind('<Button-1>', self.block_columns_resize)

    def create_sched_labelframe(self):
        self.sched_labelframe = ttk.LabelFrame(self.sched_frame, text='Schedule', style="sched.TLabelframe")
        self.create_sched_tree()
        self.create_tree_scroll()
        self.sched_labelframe.pack(fill='both', expand=True, pady=5, padx=5)

    def create_sched_tree(self):
        self.sched_tree = ttk.Treeview(self.sched_labelframe, show="headings", columns=('Hour, Event'), height=15)
        self.create_columns()
        self.sched_tree.pack(side='left', fill='both', expand=True, pady=5, padx=5)

    def create_columns(self):
        self.create_first_col()
        self.create_second_col()

    def create_first_col(self):
        self.sched_tree.column('#1')
        self.sched_tree.heading('#1', text='Hour', anchor='center')

    def create_second_col(self):
        self.sched_tree.column('#2')
        self.sched_tree.heading('#2', text='Event', anchor='center')

    def block_columns_resize(self, event):
        if self.sched_tree.identify_region(event.x, event.y) == "separator":
            return "break"
    
    def create_tree_scroll(self):
        tree_scroll = ttk.Scrollbar(self.sched_tree, orient="vertical", command=self.sched_tree.yview)
        tree_scroll.pack(side='right', fill='y')
        self.sched_tree.configure(yscrollcommand=tree_scroll.set)

    def styles(self):
        self.style = ttk.Style()
        self.style.configure("time.TFrame", background="#000")


if __name__ == '__main__':
    View()