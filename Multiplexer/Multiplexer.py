from Base.BusWire import BusWire
from LogicalElements.AndGate import AndGate
from LogicalElements.NotGate import NotGate
from LogicalElements.OrGate import OrGate


class ToWireMultiplexer:

    input_a: BusWire
    input_b: BusWire
    input_c: BusWire
    out_not_gate: BusWire
    out_and_one: BusWire
    out_and_two: BusWire
    output: BusWire
    and_gate_one: AndGate
    and_gate_two: AndGate
    or_gate_one: OrGate
    not_gate_one: NotGate

    def __init__(self):
        self.input_a: BusWire = BusWire()
        self.input_b: BusWire = BusWire()
        self.input_c: BusWire = BusWire()
        self.out_not_gate: BusWire = BusWire()
        self.out_and_one: BusWire = BusWire()
        self.out_and_two: BusWire = BusWire()
        self.output: BusWire = BusWire()
        self.and_gate_one: AndGate = AndGate()
        self.and_gate_two: AndGate = AndGate()
        self.or_gate_one: OrGate = OrGate()
        self.not_gate_one: NotGate = NotGate()

        self.not_gate_one.input.set_input(self.input_c)
        self.out_not_gate.set_input(self.not_gate_one.output)

        self.and_gate_one.input.append(self.input_a)
        self.and_gate_one.input.append(self.out_not_gate)

        self.and_gate_two.input.append(self.input_b)
        self.and_gate_two.input.append(self.input_c)

        self.out_and_one.set_input(self.and_gate_one.output)
        self.out_and_two.set_input(self.and_gate_two.output)

        self.or_gate_one.input.append(self.out_and_one)
        self.or_gate_one.input.append(self.out_and_two)

        self.output.set_input(self.or_gate_one.output)

    def set_data(self):
        self.not_gate_one.notify()
        self.and_gate_one.notify()
        self.and_gate_two.notify()
        self.or_gate_one.notify()

    def notify(self):
        self.set_data()



