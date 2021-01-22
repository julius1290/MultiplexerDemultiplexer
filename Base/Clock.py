import time
from Base.BusWire import BusWire


class Clock:

    rate: int
    notifyList: list = []
    output: BusWire = BusWire()
    stop: int

    def __init__(self, rate: int):
        self.rate = rate
        self.output.set_data(0)
        self.stop = 0

    def run(self):
        self.output.set_data(not self.output.get_data())
        #print(self.output.get_data())
        for elem in self.notifyList:
            elem.notify()
        time.sleep(1/self.rate)
        if self.stop == 0:
            self.run()

    def add_notify(self, object: any):
        self.notifyList.append(object)

    def stop_programm(self):
        self.stop = 1