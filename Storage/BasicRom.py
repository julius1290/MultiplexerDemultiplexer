from Base.BusWire import BusWire


class BasicRom:

    storage: any
    output_wire: BusWire
    size: int

    def __init__(self, length: int):
        self.size = length
        self.storage = [None for x in range(length)]
        self.output_wire = BusWire()

    def add_instruction(self, pos: int, instruction: any):
        if pos > self.size or pos < 0:
            return -1
        self.storage[pos] = instruction
        return 1

    def read_instruction(self, pos: any):
        if pos > self.size or pos < 0:
            return -1
        self.output_wire.set_data(self.storage[pos])
        return 1
