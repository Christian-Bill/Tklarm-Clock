from time import strftime


class Model:

    def __init__(self):
        pass

    def current_time_running(self, time_label):
        time_string = strftime('%I:%M:%S %p')
        time_label.config(text=time_string)
        time_label.after(1000, lambda: self.current_time_running(time_label))