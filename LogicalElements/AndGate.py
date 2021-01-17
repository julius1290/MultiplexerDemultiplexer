from Base.BusWire import BusWire


class AndGate:

    input: []
    output: BusWire()

    def __init__(self):
        self.input = []
        self.output = BusWire()

    # Bitwise and gate for n number of inputs
    def calculate(self):
        ##inputs = list(inputs)
        output: any = int(self.input[0].get_data(), 2)
        bit_len = output.bit_length()
        ##inputs.pop(0)
        for value in self.input:
            output &= int(value.get_data(), 2)
        self.output.set_data(bin(output)[2:].zfill(bit_len))
        return bin(output)[2:].zfill(bit_len)

    def notify(self):
        self.calculate()
