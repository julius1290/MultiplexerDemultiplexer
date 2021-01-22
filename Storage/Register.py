from Base.BusWire import BusWire


class Register:

    input_a: BusWire
    input_b: BusWire
    input_c: BusWire
    input_d: BusWire
    input_op: BusWire
    out_a: BusWire
    out_b: BusWire
    out_c: BusWire
    out_d: BusWire

    def __init__(self):
        self.input_a = BusWire()
        self.input_b = BusWire()
        self.input_c = BusWire()
        self.input_d = BusWire()
        self.input_op = BusWire()
        self.out_a = BusWire()
        self.out_b = BusWire()
        self.out_c = BusWire()
        self.out_d = BusWire()

    def store_a(self):
        self.out_a.set_data(self.input_a.get_data())

    def store_b(self):
        self.out_b.set_data(self.input_b.get_data())

    def store_c(self):
        self.out_c.set_data(self.input_c.get_data())

    def store_d(self):
        self.out_d.set_data(self.input_d.get_data())

    def notify(self):
        opcode = self.input_op.get_data()
        if opcode == "001":
            self.store_a()
        if opcode == "010":
            self.store_b()
        if opcode == "011":
            self.store_c()
        if opcode == "100":
            self.store_d()
