from Base.BusWire import BusWire


class InstructionCounter:

    input = BusWire()
    count = -1
    output = BusWire()
    currentinput: any = 0
    data_input = BusWire()
    op_input = BusWire()

    def notify(self):
        if self.currentinput is not self.input.get_data():
            self.currentinput = self.input.get_data()
            if int(self.op_input.get_data(), 2) == 1:
                self.count = int(self.data_input.get_data(), 2)
            else:
                self.count += 1
            self.output.set_data(self.count)
            #print("ic_out")
            #print(self.output.get_data())