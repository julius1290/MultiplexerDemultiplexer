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



class FourWireMultiplexer:

    input_a: BusWire
    input_b: BusWire
    input_c: BusWire
    input_d: BusWire
    output: BusWire
    op_a: BusWire
    op_b: BusWire
    not_a_one_to_and: BusWire
    not_a_tow_to_and: BusWire
    not_b_one_to_and: BusWire
    not_c_two_to_and: BusWire
    and_one_to_or: BusWire
    and_two_to_or: BusWire
    and_three_to_or: BusWire
    and_four_to_or: BusWire
    and_gate_one: AndGate
    not_gate_one: NotGate
    not_gate_two: NotGate
    and_gate_two: AndGate
    not_gate_three: NotGate
    and_gate_three: AndGate
    not_gate_four: NotGate
    and_gate_four: AndGate
    or_gate: OrGate

    def __init__(self):
        self.input_a = BusWire()
        self.input_b = BusWire()
        self.input_c = BusWire()
        self.input_d = BusWire()
        self.output = BusWire()
        self.op_a = BusWire()
        self.op_b = BusWire()
        self.not_a_one_to_and = BusWire()
        self.not_a_tow_to_and = BusWire()
        self.not_b_one_to_and = BusWire()
        self.not_c_two_to_and = BusWire()
        self.and_one_to_or = BusWire()
        self.and_two_to_or = BusWire()
        self.and_three_to_or = BusWire()
        self.and_four_to_or = BusWire()
        self.and_gate_one = AndGate()
        self.not_gate_one = NotGate()
        self.not_gate_two = NotGate()
        self.and_gate_two = AndGate()
        self.not_gate_three = NotGate()
        self.and_gate_three = AndGate()
        self.not_gate_four = NotGate()
        self.and_gate_four = AndGate()
        self.or_gate = OrGate()

        ##For and_gate_one
        self.not_gate_one.input.set_input(self.op_a)
        self.not_gate_two.input.set_input(self.op_b)
        self.not_a_one_to_and.set_input(self.not_gate_one.output)
        self.not_a_tow_to_and.set_input(self.not_gate_two.output)

        self.and_gate_one.input.append(self.input_a)
        self.and_gate_one.input.append(self.not_a_one_to_and)
        self.and_gate_one.input.append(self.not_a_tow_to_and)
        self.and_one_to_or.set_input(self.and_gate_one.output)

        ##For and_gate_two
        self.not_gate_three.input.set_input(self.op_a)
        self.not_b_one_to_and.set_input(self.not_gate_three.output)
        self.and_gate_two.input.append(self.not_b_one_to_and)
        self.and_gate_two.input.append(self.input_b)
        self.and_gate_two.input.append(self.op_b)
        self.and_two_to_or.set_input(self.and_gate_two.output)

        ##For and_gate_three
        self.not_gate_four.input.set_input(self.op_b)
        self.not_c_two_to_and.set_input(self.not_gate_four.output)
        self.and_gate_three.input.append(self.input_c)
        self.and_gate_three.input.append(self.not_c_two_to_and)
        self.and_gate_three.input.append(self.op_a)
        self.and_three_to_or.set_input(self.and_gate_three.output)

        ##For and_gate_four
        self.and_gate_four.input.append(self.input_d)
        self.and_gate_four.input.append(self.op_a)
        self.and_gate_four.input.append(self.op_b)
        self.and_four_to_or.set_input(self.and_gate_four.output)

        ##For or_gate
        self.or_gate.input.append(self.and_one_to_or)
        self.or_gate.input.append(self.and_two_to_or)
        self.or_gate.input.append(self.and_three_to_or)
        self.or_gate.input.append(self.and_four_to_or)
        self.output.set_input(self.or_gate.output)

    def set_data(self):
        self.not_gate_one.notify()
        self.not_gate_two.notify()
        self.not_gate_three.notify()
        self.not_gate_four.notify()

        self.and_gate_one.notify()
        self.and_gate_two.notify()
        self.and_gate_three.notify()
        self.and_gate_four.notify()

        self.or_gate.notify()

    def notify(self):
        self.set_data()
