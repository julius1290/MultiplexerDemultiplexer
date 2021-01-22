from Base.BusWire import BusWire
from LogicalElements.AndGate import AndGate
from LogicalElements.NotGate import NotGate


class FourWireDemultiplexer:

    input: BusWire
    input_op_one: BusWire
    input_op_two: BusWire
    output_a: BusWire
    output_b: BusWire
    output_c: BusWire
    output_d: BusWire
    not_one_to_and_two_one: BusWire
    not_two_to_and_three_two: BusWire
    not_three_to_and_four_one: BusWire
    not_four_to_and_four_to: BusWire
    and_gate_one: AndGate
    and_gate_two: AndGate
    and_gate_three: AndGate
    and_gate_four: AndGate
    not_gate_one: NotGate
    not_gate_two: NotGate
    not_gate_three: NotGate
    not_gate_four: NotGate

    def __init__(self):
        self.input = BusWire()
        self.input_op_one = BusWire()
        self.input_op_two = BusWire()
        self.output_a = BusWire()
        self.output_b = BusWire()
        self.output_c = BusWire()
        self.output_d = BusWire()
        self.not_one_to_and_two_one = BusWire()
        self.not_two_to_and_three_two = BusWire()
        self.not_three_to_and_four_one = BusWire()
        self.not_four_to_and_four_to = BusWire()
        self.and_gate_one = AndGate()
        self.and_gate_two = AndGate()
        self.and_gate_three = AndGate()
        self.and_gate_four = AndGate()
        self.not_gate_one = NotGate()
        self.not_gate_two = NotGate()
        self.not_gate_three = NotGate()
        self.not_gate_four = NotGate()

        #For and_gate_one
        self.and_gate_one.input.append(self.input)
        self.and_gate_one.input.append(self.input_op_one)
        self.and_gate_one.input.append(self.input_op_two)
        self.output_a.set_input(self.and_gate_one.output)

        #For and_gate_two
        self.and_gate_two.input.append(self.input)
        self.not_gate_one.input.set_input(self.input_op_one)
        self.not_one_to_and_two_one.set_input(self.not_gate_one.output)
        self.and_gate_two.input.append(self.not_one_to_and_two_one)
        self.and_gate_two.input.append(self.input_op_two)
        self.output_b.set_input(self.and_gate_two.output)

        #For and_gate_three
        self.and_gate_three.input.append(self.input)
        self.and_gate_three.input.append(self.input_op_one)
        self.not_gate_two.input.set_input(self.input_op_two)
        self.not_two_to_and_three_two.set_input(self.not_gate_two.output)
        self.and_gate_three.input.append(self.not_two_to_and_three_two)
        self.output_c.set_input(self.and_gate_three.output)

        #For and_gate_for
        self.and_gate_four.input.append(self.input)
        self.not_gate_three.input.set_input(self.input_op_one)
        self.not_gate_four.input.set_input(self.input_op_two)
        self.not_three_to_and_four_one.set_input(self.not_gate_three.output)
        self.not_four_to_and_four_to.set_input(self.not_gate_four.output)
        self.and_gate_four.input.append(self.not_three_to_and_four_one)
        self.and_gate_four.input.append(self.not_four_to_and_four_to)
        self.output_d.set_input(self.and_gate_four.output)

    def notify(self):
        self.not_gate_one.notify()
        self.not_gate_two.notify()
        self.not_gate_three.notify()
        self.not_gate_four.notify()
        self.and_gate_one.notify()
        self.and_gate_two.notify()
        self.and_gate_three.notify()
        self.and_gate_four.notify()
