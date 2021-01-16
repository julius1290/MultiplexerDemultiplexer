from Base.BusWire import BusWire


class BasicRom:

    storage: any
    output_wire: BusWire
    size: int
    input_wire: BusWire

    def __init__(self, length: int):
        self.size = length
        self.storage = [None for x in range(length)]
        self.output_wire = BusWire()
        self.input_wire = BusWire()

    def add_instruction(self, pos: int, instruction: any):
        if pos > self.size or pos < 0:
            return -1
        self.storage[pos] = instruction
        return 1

    def read_instruction(self):
        if self.input_wire.get_data() > self.size or self.input_wire.get_data() < 0:
            return -1
        self.output_wire.set_data(self.storage[self.input_wire.get_data()])
        return 1

    def notify(self):
        self.read_instruction()
        print(self.output_wire.get_data())

