from Base.BusWire import BusWire


class ConsoleOut:

    input: BusWire
    input_op: BusWire

    def __init__(self):
        self.input = BusWire()
        self.input_op = BusWire()

    def out(self):
        if self.input_op.get_data() == "1":
            character = self.input.get_data()[:1]
            data = self.input.get_data()[1:]
            if character == "1":
                print(chr(int(data, 2)))
            if character == "0":
                print(int(data, 2))

    def notify(self):
        self.out()