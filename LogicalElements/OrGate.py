from Base.BusWire import BusWire


class OrGate:
    input: [BusWire] = []
    output: [BusWire] = BusWire()

    # Bitwise and gate for n number of inputs
    def calculate(self):
        ##inputs = list(inputs)
        output: any = self.input[0].get_data()
        bit_len = output.bit_length()
        ##inputs.pop(0)
        for value in self.input:
            output |= value.get_data()
        self.output.set_data(bin(output)[2:].zfill(bit_len))
        return bin(output)[2:].zfill(bit_len)
