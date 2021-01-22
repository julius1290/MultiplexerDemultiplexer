from Base.BusWire import BusWire


class ControlUnit:

    input_wire = BusWire()
    op_output = BusWire()
    ic_output = BusWire()
    data: any

    def set_outputs(self):
        self.initOuts()
        self.data = self.input_wire.get_data()
        if self.data is not None:
            opcode = self.data[:3]
            reg_one = self.data[3:][:2]
            reg_two = self.data[5:][:2]
            charakter_bit = self.data[7:][:1]
            data_bits = self.data[8:][:8]
            self.set_op_out(opcode)
            self.set_ic_out(data_bits)

    def notify(self):
        self.set_outputs()

    def initOuts(self):
        self.ic_output.set_data(0)
        self.op_output.set_data(0)

    def set_op_out(self, opcode: any):
        if opcode == "001":
            self.op_output.set_data(1)

    def set_ic_out(self, data: any):
        self.ic_output.set_data(data)