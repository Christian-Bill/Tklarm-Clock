from view import View
from model import Model


class Controller:
    
    def __init__(self):

        self.model = Model()
        self.view = View(self)        

    def main(self):
        self.view.main()

    def fetch_current_time(self, time_label):
        self.model.current_time_running(time_label)       


if __name__ == '__main__':
    alarm_clock = Controller()
    alarm_clock.main()