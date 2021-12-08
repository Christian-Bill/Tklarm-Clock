import tkinter as tk
from tkinter import StringVar, ttk


class View(tk.Tk):

    PAD = 5
    TIME_CAPTIONS = ['AM','PM']
    BUTTONS_CAPTIONS = ['+', '-']
    TREE_HEADERS = ['Hour', 'Event']

    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        self._init_variable_holders()
        self._window_settings()
        self._window_widgets()      

    def main(self):
        self.mainloop()

    def _init_variable_holders(self):
        self.hour_value_var = StringVar()
        self.drop_value_var = StringVar()
        self.event_value_var = StringVar()
        self.minute_value_var = StringVar()

    def _window_settings(self):
        self.title('Tklarm Clock')
        self.geometry('426x562')
        self.resizable(0, 0)

    def _window_widgets(self):
        self._current_time_display()
        self._input_entries()
        self._add_delete_btns()
        self._schedules()

    def _current_time_display(self):
        '''Create Current Time Label'''
        self.time_frame = ttk.Frame(self, style="clock.TFrame")
        self._create_clock_label()
        self._pack_frame(self.time_frame)

    def _create_clock_label(self):
        time_label = ttk.Label(self.time_frame, font=("calibri", 35, "bold"),
                            anchor="center", background="black",
                            foreground="white")
        self._common_pack(time_label)
        self.controller.fetch_current_time(time_label)

    def _input_entries(self):
        self._input_time_entry()
        self._input_event_entry()

    def _input_time_entry(self):
        '''Create Input Time Frame'''
        self.input_time_frame = ttk.Frame(self, style="entries.TFrame")
        self._render_input_time_entries()
        self._pack_frame(self.input_time_frame)

    def _render_input_time_entries(self):
        self._input_hour_entry()
        self._input_minute_entry()
        self._input_am_pm()

    def _input_hour_entry(self):
        self.hour_frame = ttk.LabelFrame(self.input_time_frame, text='Hour', style="event.TLabelframe")
        self.hour_entry = ttk.Entry(self.hour_frame, width=15, textvariable=self.hour_value_var)
        self._pack_input_widgets(self.hour_entry, self.hour_frame, side='left')

    def _input_minute_entry(self):
        self.minute_frame = ttk.LabelFrame(self.input_time_frame, text='Minute', style="event.TLabelframe")
        self.minute_entry = ttk.Entry(self.minute_frame, width=15, textvariable=self.minute_value_var)
        self._pack_input_widgets(self.minute_entry, self.minute_frame, side='left')

    def _input_am_pm(self):
        self.am_pm_frame = ttk.LabelFrame(self.input_time_frame, text='AM-PM', style="event.TLabelframe")
        drop = ttk.Combobox(self.am_pm_frame, textvariable=self.drop_value_var, value=self.TIME_CAPTIONS, state='readonly')
        drop.current(0)
        self._pack_input_widgets(drop, self.am_pm_frame, side='left')

    def _input_event_entry(self):
        '''Create Input Event Entry'''
        self.input_event_frame = ttk.Frame(self, style="entries.TFrame")
        self.render_input_event_entry()
        self._pack_frame(self.input_event_frame)

    def render_input_event_entry(self):
        self.event_labelframe = ttk.LabelFrame(self.input_event_frame, text='Event', style="event.TLabelframe")
        self.event_entry = ttk.Entry(self.event_labelframe, textvariable=self.event_value_var)
        self._pack_input_widgets(self.event_entry, self.event_labelframe)

    def _pack_input_widgets(self, widget1, widget2, side=None):
        self._common_pack(widget1)
        self._common_pack(widget2, side=side)

    def _add_delete_btns(self):
        '''Create Add and Delete Buttons'''
        self.btns_frame = ttk.Frame(self, height='5', style="entries.TFrame")
        self._create_btn_labelframe()
        self._pack_frame(self.btns_frame)

    def _create_btn_labelframe(self):
        self.btns_labelframe = ttk.LabelFrame(self.btns_frame, text='Controls', style="btn.TLabelframe")
        self._display_buttons()
        self._common_pack(self.btns_labelframe)

    def _display_buttons(self):
        for text in self.BUTTONS_CAPTIONS:
            btn = ttk.Button(self.btns_labelframe, text=f'{text}', style="btn.TButton")
            self._common_pack(btn, side='left')

    def _schedules(self):
        '''Create Schedules Treeview'''
        self.sched_frame = ttk.Frame(self, style="sched.TFrame")
        self._create_sched_labelframe()
        self._pack_frame(self.sched_frame, expand=True)
        self.sched_tree.bind('<Button-1>', self._block_resize_column)

    def _create_sched_labelframe(self):
        self.sched_labelframe = ttk.LabelFrame(self.sched_frame, text='Schedule', style="sched.TLabelframe")
        self._create_sched_tree()
        self._create_scrolls()
        self._common_pack(self.sched_labelframe)

    def _create_scrolls(self):
        self._create_tree_yscroll()
        self._create_tree_xscroll()

    def _create_sched_tree(self):
        self.sched_tree = ttk.Treeview(self.sched_labelframe, show="headings", columns=('Hour, Event'), height=15)
        self._create_columns()
        self._common_pack(self.sched_tree, side='left')

    def _create_columns(self):
        column_title = 0
        for index in range(1, len(self.TREE_HEADERS)+1):
            self.sched_tree.column(f'#{index}')
            self.sched_tree.heading(f'#{index}', text=f'{self.TREE_HEADERS[column_title]}', anchor='center')
            column_title += 1

    def _block_resize_column(self, event):
        if self.sched_tree.identify_region(event.x, event.y) == "separator":
            return "break"
    
    def _create_tree_yscroll(self):
        tree_yscroll = ttk.Scrollbar(self.sched_tree, orient="vertical", command=self.sched_tree.yview)
        tree_yscroll.pack(side='right', fill='y')
        self.sched_tree.configure(yscrollcommand=tree_yscroll.set)

    def _create_tree_xscroll(self):
        tree_xscroll = ttk.Scrollbar(self.sched_tree, orient="horizontal", command=self.sched_tree.xview)
        tree_xscroll.pack(side='bottom', fill='x')
        self.sched_tree.configure(xscrollcommand=tree_xscroll.set)

    def _common_pack(self, widget, side=None):
        widget.pack(side=side, fill='both', expand=True, pady=self.PAD, padx=self.PAD)

    def _pack_frame(self, widget, expand=None, padx=None, pady=None):
        widget.pack(side='top', fill='both', expand=expand, padx=padx, pady=pady)

    def _styles(self):
        self.style = ttk.Style()
        self.style.configure("clock.TFrame", background="#000")