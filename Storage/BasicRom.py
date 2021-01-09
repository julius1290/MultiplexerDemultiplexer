from Base.BusWire import BusWire


class BasicRom:

    storage: any
    output_wire: BusWire

    def __init__(self, length: int):
        self.storage = [None for x in range(length)]
        self.output_wire = BusWire()

    def add_instruction(self, pos: int, instruction: any):
        self.storage[pos] = instruction

    def read_instruction(self, pos: any):
        self.output_wire.set_data(self.storage[pos])
