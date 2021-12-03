from time import strftime

def fetch_current_time(time_label):
    """To recursively display time"""
    time_string = strftime('%I:%M:%S %p')
    time_label.config(text=time_string)
    time_label.after(1000, lambda: fetch_current_time(time_label))
