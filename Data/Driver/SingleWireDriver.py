from Base.BusWire import BusWire
from LogicalElements.AndGate import AndGate


class SingleWireDriver:

    input_data: BusWire
    input_driver: BusWire
    output: BusWire
    and_gate: AndGate

    def __init__(self):
        self.input_data = BusWire()
        self.input_driver = BusWire()
        self.output = BusWire()
        self.and_gate = AndGate()

        self.and_gate.input.append(self.input_data)
        self.and_gate.input.append(self.input_driver)
        self.output.set_input(self.and_gate.output)

    def notify(self):
        self.and_gate.notify()