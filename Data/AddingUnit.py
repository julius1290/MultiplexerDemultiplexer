from Base.BusWire import BusWire


class AddingUnit:

    input_a: BusWire
    input_b: BusWire
    output: BusWire

    def __init__(self):
        self.input_a = BusWire()
        self.input_b = BusWire()
        self.output = BusWire()

    def add(self):
        result = int(self.input_a.get_data(), 2) + int(self.input_b.get_data(), 2)
        out = bin(result)[2:].zfill(8)
        self.output.set_data(out)

    def notify(self):
        self.add()