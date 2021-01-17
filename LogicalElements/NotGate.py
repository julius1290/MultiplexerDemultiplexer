from Base.BusWire import BusWire


class NotGate:
    input: [BusWire] = BusWire()
    output: [BusWire] = BusWire()

    # Bitwise and gate for n number of inputs
    def calculate(self):
        ##inputs = list(inputs)
        ##output: any = self.input.get_data()
        bit_len = 8
        mask = int("11111111", 2)
        ##inputs.pop(0)
        output = ~self.input.get_data() & mask
        self.output.set_data(bin(output)[2:].zfill(bit_len))
        return bin(output)[2:].zfill(bit_len)