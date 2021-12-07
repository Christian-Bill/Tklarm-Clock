# from model import Model
from view import View

class Controller:
    def __init__(self):

        self.view = View(self)
        # self.model = Model(self)

    def main(self):
        self.view.main()


if __name__ == '__main__':
    alarm_clock = Controller()
    alarm_clock.main()