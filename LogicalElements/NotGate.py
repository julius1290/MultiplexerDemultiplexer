from Base.BusWire import BusWire


class NotGate:
    input: BusWire
    output: BusWire

    def __init__(self):
        self.input = BusWire()
        self.output = BusWire()

    # Bitwise and gate for n number of inputs
    def calculate(self):
        ##inputs = list(inputs)
        ##output: any = self.input.get_data()
        bit_len = 8
        mask = int("11111111", 2)
        ##inputs.pop(0)
        output = ~int(self.input.get_data(), 2) & mask
        self.output.set_data(bin(output)[2:].zfill(8))
        ##self.output.set_data(output)
        return bin(output)[2:].zfill(8)

    def notify(self):
        self.calculate()