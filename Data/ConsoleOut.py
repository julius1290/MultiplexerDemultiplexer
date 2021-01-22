from Base.BusWire import BusWire


class ConsoleOut:

    input: BusWire
    input_op: BusWire

    def __init__(self):
        self.input = BusWire()
        self.input_op = BusWire()

    def out(self):
        if self.input_op == "1":
            character = self.input[:1]
            data = self.input[1:]
            if character == "1":
                print(chr(int(data, 2)))
