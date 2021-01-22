from Base.BusWire import BusWire
from Base.Clock import Clock
from Data.AddingUnit import AddingUnit
from Data.ConsoleOut import ConsoleOut
from Data.Driver.SingleWireDriver import SingleWireDriver
from Data.Driver.ThreeWireDiver import ThreeWireDriver
from Multiplexer.FourWireDemultiplexer import FourWireDemultiplexer
from Multiplexer.FourWireMultiplexer import FourWireMultiplexer
from Multiplexer.TwoWireDemultiplexer import TwoWireDemultiplexer
from Storage.BasicRam import BasicRam
from Storage.BasicRom import BasicRom
from Storage.Register import Register


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

    four_wire_multiplexer: FourWireMultiplexer
    four_wire_demultiplexer: FourWireDemultiplexer
    console_out: ConsoleOut
    single_wire_driver: SingleWireDriver
    three_wire_driver: ThreeWireDriver
    two_wire_demultiplexer: TwoWireDemultiplexer
    ram: BasicRam
    adding_unit: AddingUnit
    register: Register
    opcode: str
    reg_one: str
    reg_two: str
    data: any
    clock: Clock

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

        self.four_wire_multiplexer = None
        self.four_wire_demultiplexer = None
        self.register = None
        self.two_wire_demultiplexer = None
        self.ram = None
        self.adding_unit = None
        self.single_wire_driver = None
        self.three_wire_driver = None
        self.console_out = None
        self.clock= None

        self.opcode = ""
        self.reg_one = ""
        self.reg_two = ""
        self.data = ""


    def set_outputs(self):
        self.resetOuts()
        self.data = self.input_wire.get_data()
        #print("this is data")
        #print(self.input_wire.get_data())
        if self.data is not None:
            self.opcode = self.data[:3]
            self.reg_one = self.data[3:][:2]
            self.reg_two = self.data[5:][:2]
            charakter_bit = self.data[7:][:1]
            self.data = self.data[8:][:8]
        self.choose_instruction()


    def notify(self):
        self.set_outputs()

    def resetOuts(self):
        self.ic_out_op.set_data("00000000")
        self.ic_out_data.set_data("00000000")

        self.reg_demux_op_a.set_data("00000000")
        self.reg_demux_op_b.set_data("00000000")
        self.reg_op.set_data("00000000")
        self.reg_mux_op_a.set_data("00000000")
        self.reg_mux_op_b.set_data("00000000")

        self.reg_to_adding_driver_out_op.set_data("00000000")
        self.reg_to_adding_ram_demux_out_o.set_data("00000000")
        self.cout_out_op.set_data("00000000")
        self.addi_out_data.set_data("00000000")
        self.ram_out_adress.set_data("00000000")
        self.ram_out_op.set_data("00000000")
        self.ldi_out_data.set_data("00000000")
        self.adding_ldi_ram_driver_out_op_a.set_data("00000000")
        self.adding_ldi_ram_driver_out_op_b.set_data("00000000")
        self.adding_ldi_ram_driver_out_op_c.set_data("00000000")

    def choose_instruction(self):
        if self.opcode == "001":
            self.load_from_ram()
        if self.opcode == "010":
            self.load_immidiate()
        if self.opcode == "011":
            self.add_immidiate()
        if self.opcode == "100":
            self.store()
        if self.opcode == "101":
            self.console_print()
        if self.opcode == "000":
            self.register_copy()
        if self.opcode == "111":
            self.exit_programm()

    def set_ic_out(self, data: any):
        self.ic_output.set_data(data)

    def load_immidiate(self):
        self.resetOuts()
        self.ldi_out_data.set_data(self.data)
        self.adding_ldi_ram_driver_out_op_a.set_data("11111111")
        self.adding_ldi_ram_driver_out_op_b.set_data("00000000")
        self.adding_ldi_ram_driver_out_op_c.set_data("00000000")
        choosen_reg = int(self.reg_one, 2)
        if choosen_reg == 0:
            self.reg_demux_op_a.set_data("11111111")
            self.reg_demux_op_b.set_data("11111111")
            self.reg_op.set_data("001")
        if choosen_reg == 1:
            self.reg_demux_op_a.set_data("00000000")
            self.reg_demux_op_b.set_data("11111111")
            self.reg_op.set_data("010")
        if choosen_reg == 2:
            self.reg_demux_op_a.set_data("11111111")
            self.reg_demux_op_b.set_data("00000000")
            self.reg_op.set_data("011")
        if choosen_reg == 3:
            self.reg_demux_op_a.set_data("00000000")
            self.reg_demux_op_b.set_data("00000000")
            self.reg_op.set_data("100")
        self.three_wire_driver.notify()
        self.four_wire_demultiplexer.notify()
        self.register.notify()

    def add_immidiate(self):
        self.resetOuts()
        self.adding_ldi_ram_driver_out_op_a.set_data("00000000")
        self.adding_ldi_ram_driver_out_op_b.set_data("11111111")
        self.adding_ldi_ram_driver_out_op_c.set_data("00000000")
        self.addi_out_data.set_data(self.data)
        self.reg_to_adding_driver_out_op.set_data("11111111")
        choosen_reg = int(self.reg_one, 2)
        if choosen_reg == 0:
            self.reg_demux_op_a.set_data("11111111")
            self.reg_demux_op_b.set_data("11111111")
            self.reg_mux_op_a.set_data("00000000")
            self.reg_mux_op_b.set_data("00000000")
            self.reg_op.set_data("001")
        if choosen_reg == 1:
            self.reg_demux_op_a.set_data("00000000")
            self.reg_demux_op_b.set_data("11111111")
            self.reg_mux_op_a.set_data("00000000")
            self.reg_mux_op_b.set_data("11111111")
            self.reg_op.set_data("010")
        if choosen_reg == 2:
            self.reg_demux_op_a.set_data("11111111")
            self.reg_demux_op_b.set_data("00000000")
            self.reg_mux_op_a.set_data("11111111")
            self.reg_mux_op_b.set_data("00000000")
            self.reg_op.set_data("011")
        if choosen_reg == 3:
            self.reg_demux_op_a.set_data("00000000")
            self.reg_demux_op_b.set_data("00000000")
            self.reg_mux_op_a.set_data("11111111")
            self.reg_mux_op_b.set_data("11111111")
            self.reg_op.set_data("100")

        self.reg_to_adding_ram_demux_out_o.set_data("11111111")
        self.four_wire_multiplexer.notify()
        self.single_wire_driver.notify()
        self.two_wire_demultiplexer.notify()
        self.adding_unit.notify()
        self.three_wire_driver.notify()
        self.four_wire_demultiplexer.notify()
        self.register.notify()

    def store(self):
        self.resetOuts()
        self.reg_to_adding_driver_out_op.set_data("11111111")
        self.reg_to_adding_ram_demux_out_o.set_data("00000000")

        choosen_reg = int(self.reg_one, 2)
        if choosen_reg == 0:
            self.reg_mux_op_a.set_data("00000000")
            self.reg_mux_op_b.set_data("00000000")
        if choosen_reg == 1:
            self.reg_mux_op_a.set_data("00000000")
            self.reg_mux_op_b.set_data("11111111")
        if choosen_reg == 2:
            self.reg_mux_op_a.set_data("11111111")
            self.reg_mux_op_b.set_data("00000000")
        if choosen_reg == 3:
            self.reg_mux_op_a.set_data("11111111")
            self.reg_mux_op_b.set_data("11111111")

        self.ram_out_adress.set_data(self.data)
        self.ram_out_op.set_data("10")
        self.four_wire_multiplexer.notify()
        self.single_wire_driver.notify()
        self.two_wire_demultiplexer.notify()
        self.ram.notify()

    def console_print(self):
        self.resetOuts()
        self.reg_to_adding_driver_out_op.set_data("11111111")
        self.reg_to_adding_ram_demux_out_o.set_data("00000000")

        choosen_reg = int(self.reg_one, 2)
        if choosen_reg == 0:
            self.reg_mux_op_a.set_data("00000000")
            self.reg_mux_op_b.set_data("00000000")
        if choosen_reg == 1:
            self.reg_mux_op_a.set_data("00000000")
            self.reg_mux_op_b.set_data("11111111")
        if choosen_reg == 2:
            self.reg_mux_op_a.set_data("11111111")
            self.reg_mux_op_b.set_data("00000000")
        if choosen_reg == 3:
            self.reg_mux_op_a.set_data("11111111")
            self.reg_mux_op_b.set_data("11111111")
        self.cout_out_op.set_data("1")
        self.four_wire_multiplexer.notify()
        self.single_wire_driver.notify()
        self.two_wire_demultiplexer.notify()
        self.console_out.notify()

    def load_from_ram(self):
        self.resetOuts()
        self.ldi_out_data.set_data(self.data)
        self.adding_ldi_ram_driver_out_op_a.set_data("00000000")
        self.adding_ldi_ram_driver_out_op_b.set_data("00000000")
        self.adding_ldi_ram_driver_out_op_c.set_data("11111111")
        choosen_reg = int(self.reg_one, 2)
        if choosen_reg == 0:
            self.reg_demux_op_a.set_data("11111111")
            self.reg_demux_op_b.set_data("11111111")
            self.reg_op.set_data("001")
        if choosen_reg == 1:
            self.reg_demux_op_a.set_data("00000000")
            self.reg_demux_op_b.set_data("11111111")
            self.reg_op.set_data("010")
        if choosen_reg == 2:
            self.reg_demux_op_a.set_data("11111111")
            self.reg_demux_op_b.set_data("00000000")
            self.reg_op.set_data("011")
        if choosen_reg == 3:
            self.reg_demux_op_a.set_data("00000000")
            self.reg_demux_op_b.set_data("00000000")
            self.reg_op.set_data("100")
        self.ram_out_adress.set_data(self.data)
        self.ram_out_op.set_data("11")
        self.ram.notify()
        self.three_wire_driver.notify()
        self.four_wire_demultiplexer.notify()
        self.register.notify()

    def register_copy(self):
        self.resetOuts()
        self.adding_ldi_ram_driver_out_op_a.set_data("00000000")
        self.adding_ldi_ram_driver_out_op_b.set_data("11111111")
        self.adding_ldi_ram_driver_out_op_c.set_data("00000000")
        self.addi_out_data.set_data("00000000")
        self.reg_to_adding_driver_out_op.set_data("11111111")
        choosen_reg_dest = int(self.reg_one, 2)
        choosen_reg_src = int(self.reg_two, 2)
        if choosen_reg_src == 0:
            self.reg_mux_op_a.set_data("00000000")
            self.reg_mux_op_b.set_data("00000000")
        if choosen_reg_src == 1:
            self.reg_mux_op_a.set_data("00000000")
            self.reg_mux_op_b.set_data("11111111")
        if choosen_reg_src == 2:
            self.reg_mux_op_a.set_data("11111111")
            self.reg_mux_op_b.set_data("00000000")
        if choosen_reg_src == 3:
            self.reg_mux_op_a.set_data("11111111")
            self.reg_mux_op_b.set_data("11111111")
        if choosen_reg_dest == 0:
            self.reg_demux_op_a.set_data("11111111")
            self.reg_demux_op_b.set_data("11111111")
            self.reg_op.set_data("001")
        if choosen_reg_dest == 1:
            self.reg_demux_op_a.set_data("00000000")
            self.reg_demux_op_b.set_data("11111111")
            self.reg_op.set_data("010")
        if choosen_reg_dest == 2:
            self.reg_demux_op_a.set_data("11111111")
            self.reg_demux_op_b.set_data("00000000")
            self.reg_op.set_data("011")
        if choosen_reg_dest == 3:
            self.reg_demux_op_a.set_data("00000000")
            self.reg_demux_op_b.set_data("00000000")
            self.reg_op.set_data("100")
        self.reg_to_adding_ram_demux_out_o.set_data("11111111")
        self.four_wire_multiplexer.notify()
        self.single_wire_driver.notify()
        self.two_wire_demultiplexer.notify()
        self.adding_unit.notify()
        self.three_wire_driver.notify()
        self.four_wire_demultiplexer.notify()
        self.register.notify()
        print("yeah6")

    def exit_programm(self):
        self.clock.stop_programm()