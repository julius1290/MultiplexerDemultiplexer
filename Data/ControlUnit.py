from Base.BusWire import BusWire


class ControlUnit:

    input_wire: BusWire

    ic_out_op: BusWire
    ic_out_data: BusWire

    reg_demux_op_a: BusWire
    reg_demux_op_b: BusWire
    reg_op: BusWire
    reg_mux_op_a: BusWire
    reg_mux_op_b: BusWire

    reg_to_adding_driver_out_op: BusWire
    reg_to_adding_ram_demux_out_o: BusWire
    cout_out_op: BusWire
    addi_out_data: BusWire
    ram_out_adress: BusWire
    ram_out_op: BusWire
    ldi_out_data: BusWire
    adding_ldi_ram_driver_out_op_a: BusWire
    adding_ldi_ram_driver_out_op_b: BusWire
    adding_ldi_ram_driver_out_op_c: BusWire

    data: any

    def __init__(self):
        self.input_wire = BusWire()

        self.ic_out_op = BusWire()
        self.ic_out_data = BusWire()

        self.reg_demux_op_a = BusWire()
        self.reg_demux_op_b = BusWire()
        self.reg_op = BusWire()
        self.reg_mux_op_a = BusWire()
        self.reg_mux_op_b = BusWire()

        self.reg_to_adding_driver_out_op = BusWire()
        self.reg_to_adding_ram_demux_out_o = BusWire()
        self.cout_out_op = BusWire()
        self.addi_out_data = BusWire()
        self.ram_out_adress = BusWire()
        self.ram_out_op = BusWire()
        self.ldi_out_data = BusWire()
        self.adding_ldi_ram_driver_out_op_a = BusWire()
        self.adding_ldi_ram_driver_out_op_b = BusWire()
        self.adding_ldi_ram_driver_out_op_c = BusWire()


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