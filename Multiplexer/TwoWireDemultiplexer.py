from Base.BusWire import BusWire
from LogicalElements.AndGate import AndGate
from LogicalElements.NotGate import NotGate


class TwoWireDemultiplexer:

    input: BusWire
    input_op: BusWire
    output_a: BusWire
    output_b: BusWire
    not_to_and: BusWire
    and_gate_one: AndGate
    and_gate_two: AndGate
    not_gate: NotGate

    def __init__(self):
        self.input = BusWire()
        self.input_op = BusWire()
        self.output_a = BusWire()
        self.output_b = BusWire()
        self.not_to_and = BusWire()
        self.and_gate_one = AndGate()
        self.and_gate_two = AndGate()
        self.not_gate = NotGate()

        self.not_gate.input.set_input(self.input_op)
        self.not_to_and.set_input(self.not_gate.output)
        self.and_gate_one.input.append(self.input)
        self.and_gate_one.input.append(self.input_op)

        self.and_gate_two.input.append(self.input)
        self.and_gate_two.input.append(self.not_to_and)

        self.output_a.set_input(self.and_gate_one.output)
        self.output_b.set_input(self.and_gate_two.output)

    def notify(self):
        self.not_gate.notify()
        self.and_gate_one.notify()
        self.and_gate_two.notify()