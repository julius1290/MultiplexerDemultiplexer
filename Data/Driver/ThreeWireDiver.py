from Base.BusWire import BusWire
from LogicalElements.AndGate import AndGate
from LogicalElements.OrGate import OrGate


class ThreeWireDriver:

    input_a: BusWire
    input_b: BusWire
    input_c: BusWire
    output: BusWire
    input_driver_a: BusWire
    input_driver_b: BusWire
    input_driver_c: BusWire
    and_gate_one_to_or: BusWire
    and_gate_two_to_or: BusWire
    and_gate_three_to_or: BusWire
    and_gate_one: AndGate
    and_gate_two: AndGate
    and_gate_three: AndGate
    or_gate: OrGate

    def __init__(self):
        self.input_a = BusWire()
        self.input_b = BusWire()
        self.input_c = BusWire()
        self.and_gate_one_to_or = BusWire()
        self.and_gate_two_to_or = BusWire()
        self.and_gate_three_to_or = BusWire()
        self.input_driver_a = BusWire()
        self.input_driver_b = BusWire()
        self.input_driver_c = BusWire()
        self.output = BusWire()

        self.and_gate_one.input.append(self.input_a)
        self.and_gate_one.input.append(self.input_driver_a)
        self.and_gate_one_to_or.set_input(self.and_gate_one.output)

        self.and_gate_two.input.append(self.input_b)
        self.and_gate_two.input.append(self.input_driver_b)
        self.and_gate_two_to_or.set_input(self.and_gate_two.output)

        self.and_gate_three.input.append(self.input_c)
        self.and_gate_three.input.append(self.input_driver_c)
        self.and_gate_three_to_or.set_input(self.and_gate_three.output)

        self.or_gate.input.append(self.and_gate_one_to_or)
        self.or_gate.input.append(self.and_gate_two_to_or)
        self.or_gate.input.append(self.and_gate_three_to_or)

        self.output.set_input(self.or_gate.output)

    def notify(self):
        self.and_gate_one.notify()
        self.and_gate_two.notify()
        self.and_gate_three.notify()
        self.or_gate.notify()
