from Base.BusWire import BusWire


class InstructionCounter:

    input = BusWire()
    count = -1
    output = BusWire()
    currentinput: any = 0

    def notify(self):
        if self.currentinput is not self.input.get_data():
            self.currentinput = self.input.get_data()
            self.count +=1
            self.output.set_data(self.count)
            print(self.output.get_data())