from Base.Clock import Clock
from Storage.Register import Register
from Storage.BasicRom import BasicRom
from Storage.BasicRam import BasicRam
from Multiplexer.Multiplexer import ToWireMultiplexer
from Multiplexer.FourWireMultiplexer import FourWireMultiplexer
from Multiplexer.FourWireDemultiplexer import FourWireDemultiplexer
from Multiplexer.TwoWireDemultiplexer import TwoWireDemultiplexer
from Data.ControlUnit import ControlUnit
from Data.InstructionCounter import InstructionCounter
from Data.AddingUnit import AddingUnit
from Data.Driver.SingleWireDriver import SingleWireDriver
from Data.Driver.ThreeWireDiver import ThreeWireDriver
from Data.ConsoleOut import ConsoleOut
from Base.BusWire import BusWire

class ProcessorSystem:

    clock: Clock
    instruction_counter: InstructionCounter
    rom: BasicRom
    control_unit: ControlUnit
    ram: BasicRam
    adding_unit: AddingUnit
    register: Register
    reg_multiplexer: FourWireMultiplexer
    reg_demultiplexer: FourWireDemultiplexer
    console_out: ConsoleOut
    adding_ram_demux: TwoWireDemultiplexer
    reg_to_ram_adding_driver: SingleWireDriver
    adding_ldi_ram_to_data_driver: ThreeWireDriver

    clock_to_ic: BusWire
    ic_to_rom: BusWire
    rom_to_cu: BusWire
    cu_to_ic_data: BusWire
    cu_to_ic_op: BusWire
    cu_to_reg_demux_op_a: BusWire
    cu_to_reg_demux_op_b: BusWire
    cu_to_reg_op: BusWire
    cu_to_reg_mux_op_a: BusWire
    cu_to_reg_mux_op_b: BusWire
    cu_to_adding_ram_driver_op: BusWire
    cu_to_adding_ram_demux: BusWire
    cu_to_cout_op: BusWire
    cu_to_ram_adress: BusWire
    cu_to_ram_op: BusWire
    cu_to_adding_ldi_ram_driver_in_a: BusWire
    cu_to_adding_ldi_ram_driver_op_a: BusWire
    cu_to_adding_ldi_ram_driver_op_b: BusWire
    cu_to_adding_ldi_ram_driver_op_c: BusWire
    cu_to_adding_data: BusWire
    adding_ldi_ram_to_reg_demux: BusWire
    reg_demux_out_a_to_reg_a: BusWire
    reg_demux_out_b_to_reg_b: BusWire
    reg_demux_out_c_to_reg_c: BusWire
    reg_demux_out_d_to_reg_d: BusWire
    reg_out_a_to_reg_mux_in_a: BusWire
    reg_out_b_to_reg_mux_in_b: BusWire
    reg_out_c_to_reg_mux_in_c: BusWire
    reg_out_d_to_reg_mux_in_d: BusWire
    reg_mux_out_to_adding_ram_driver: BusWire
    adding_ram_driver_to_adding_ram_demux_in: BusWire
    adding_ram_demux_out_a_to_adding: BusWire
    adding_ram_demux_out_b_to_ram: BusWire
    adding_to_adding_ldi_ram_driver_in_b: BusWire
    ram_to_adding_ldi_ram_in_c: BusWire

    def __init__(self):
        self.clock = Clock()
        self.instruction_counter = InstructionCounter()
        self.rom = BasicRom()
        self.control_unit = ControlUnit()
        self.ram = BasicRam()
        self.adding_unit = AddingUnit()
        self.register = Register()
        self.reg_multiplexer = FourWireMultiplexer()
        self.reg_demultiplexer = FourWireDemultiplexer()
        self.console_out = ConsoleOut()
        self.adding_ram_demux = TwoWireDemultiplexer()
        self.reg_to_ram_adding_driver = SingleWireDriver()
        self.adding_ldi_ram_to_data_driver = ThreeWireDriver()

        self.clock_to_ic = BusWire()
        self.ic_to_rom = BusWire()
        self.rom_to_cu = BusWire()
        self.cu_to_ic_data = BusWire()
        self.cu_to_ic_op = BusWire()
        self.cu_to_reg_demux_op_a = BusWire()
        self.cu_to_reg_demux_op_b = BusWire()
        self.cu_to_reg_op = BusWire()
        self.cu_to_reg_mux_op_a = BusWire()
        self.cu_to_reg_mux_op_b = BusWire()
        self.cu_to_adding_ram_driver_op = BusWire()
        self.cu_to_adding_ram_demux = BusWire()
        self.cu_to_cout_op = BusWire()
        self.cu_to_ram_adress = BusWire()
        self.cu_to_ram_op = BusWire()
        self.cu_to_adding_ldi_ram_driver_in_a = BusWire()
        self.cu_to_adding_ldi_ram_driver_op_a = BusWire()
        self.cu_to_adding_ldi_ram_driver_op_b = BusWire()
        self.cu_to_adding_ldi_ram_driver_op_c = BusWire()
        self.cu_to_adding_data = BusWire()
        self.adding_ldi_ram_to_reg_demux = BusWire()
        self.reg_demux_out_a_to_reg_a = BusWire()
        self.reg_demux_out_b_to_reg_b = BusWire()
        self.reg_demux_out_c_to_reg_c = BusWire()
        self.reg_demux_out_d_to_reg_d = BusWire()
        self.reg_out_a_to_reg_mux_in_a = BusWire()
        self.reg_out_b_to_reg_mux_in_b = BusWire()
        self.reg_out_c_to_reg_mux_in_c = BusWire()
        self.reg_out_d_to_reg_mux_in_d = BusWire()
        self.reg_mux_out_to_adding_ram_driver = BusWire()
        self.adding_ram_driver_to_adding_ram_demux_in = BusWire()
        self.adding_ram_demux_out_a_to_adding = BusWire()
        self.adding_ram_demux_out_b_to_ram = BusWire()
        self.adding_to_adding_ldi_ram_driver_in_b = BusWire()
        self.ram_to_adding_ldi_ram_in_c = BusWire()

        self.clock_to_ic.set_input(self.clock.output)
        self.instruction_counter.input.set_input(self.clock_to_ic)

        self.ic_to_rom.set_input(self.instruction_counter.output)
        self.rom.input_wire.set_input(self.ic_to_rom)

        self.rom_to_cu.set_input(self.rom.output_wire)
        self.control_unit.input_wire.set_input(self.rom_to_cu)

        self.cu_to_ic_op.set_input(self.control_unit.ic_out_op)
        self.instruction_counter.op_input.set_input(self.cu_to_ic_op)

        self.cu_to_ic_data.set_input(self.control_unit.ic_out_data)
        self.instruction_counter.data_input(self.cu_to_ic_data)

        #
        self.cu_to_reg_demux_op_a.set_input(self.control_unit.reg_demux_op_a)
        self.reg_demultiplexer.input_op_one.set_input(self.cu_to_reg_demux_op_a)

        self.cu_to_reg_demux_op_b.set_input(self.control_unit.reg_demux_op_b)
        self.reg_demultiplexer.input_op_two.set_input(self.cu_to_reg_demux_op_b)

        self.cu_to_reg_mux_op_a.set_input(self.control_unit.reg_mux_op_a)
        self.reg_multiplexer.op_a.set_input(self.cu_to_reg_mux_op_a)

        self.cu_to_reg_mux_op_b.set_input(self.control_unit.reg_mux_op_b)
        self.reg_multiplexer.op_b.set_input(self.cu_to_reg_mux_op_b)

        self.reg_demux_out_a_to_reg_a.set_input(self.reg_demultiplexer.output_a)
        self.register.input_a.set_input(self.reg_demux_out_a_to_reg_a)

        self.reg_demux_out_b_to_reg_b.set_input(self.reg_demultiplexer.output_a)
        self.register.input_b.set_input(self.reg_demux_out_b_to_reg_b)

        self.reg_demux_out_c_to_reg_c.set_input(self.reg_demultiplexer.output_c)
        self.register.input_c.set_input(self.reg_demux_out_c_to_reg_c)

        self.reg_demux_out_d_to_reg_d.set_input(self.reg_demultiplexer.output_d)
        self.register.input_d.set_input(self.reg_demux_out_d_to_reg_d)

        self.cu_to_reg_op.set_input(self.control_unit.reg_op)
        self.register.input_op.set_input(self.cu_to_reg_op)

        self.reg_out_a_to_reg_mux_in_a.set_input(self.register.out_a)
        self.reg_multiplexer.input_a.set_input(self.reg_out_a_to_reg_mux_in_a)

        self.reg_out_b_to_reg_mux_in_b.set_input(self.register.out_b)
        self.reg_multiplexer.input_b.set_input(self.reg_out_b_to_reg_mux_in_b)

        self.reg_out_c_to_reg_mux_in_c.set_input(self.register.out_c)
        self.reg_multiplexer.input_c.set_input(self.reg_out_c_to_reg_mux_in_c)

        self.reg_out_d_to_reg_mux_in_d.set_input(self.register.out_d)
        self.reg_multiplexer.input_d.set_input(self.reg_out_d_to_reg_mux_in_d)

        self.reg_mux_out_to_adding_ram_driver.set_input(self.reg_multiplexer.output)
        self.reg_to_ram_adding_driver.input_data.set_input(self.reg_mux_out_to_adding_ram_driver)

        self.cu_to_adding_ram_driver_op.set_input(self.control_unit.reg_to_adding_driver_out_op)
        self.reg_to_ram_adding_driver.input_driver.set_input(self.cu_to_adding_ram_driver_op)

        self.adding_ram_driver_to_adding_ram_demux_in.set_input(self.reg_to_ram_adding_driver.output)
        self.adding_ram_demux.input.set_input(self.adding_ram_driver_to_adding_ram_demux_in)

        self.cu_to_adding_ram_demux.set_input(self.control_unit.reg_to_adding_ram_demux_out_o)
        self.adding_ram_demux.input_op.set_input(self.cu_to_adding_ram_demux)

        self.adding_ram_demux_out_a_to_adding.set_input(self.adding_ram_demux.output_a)
        self.adding_unit.input_a.set_input(self.adding_ram_demux_out_a_to_adding)

        self.cu_to_adding_data.set_input(self.control_unit.addi_out_data)
        self.adding_unit.input_b.set_input(self.cu_to_adding_data)

        self.adding_ram_demux_out_b_to_ram.set_input(self.adding_ram_demux.output_b)
        self.ram.input.set_input(self.adding_ram_demux_out_b_to_ram)
        self.console_out.input.set_input(self.adding_ram_demux_out_b_to_ram)

        self.cu_to_cout_op.set_input(self.control_unit.cout_out_op)
        self.console_out.input_op.set_input(self.cu_to_cout_op)

        self.cu_to_ram_op.set_input(self.control_unit.ram_out_op)
        self.ram.opcode.set_input(self.cu_to_ram_op)

        self.cu_to_ram_adress.set_input(self.control_unit.ram_out_adress)
        self.ram.address.set_input(self.cu_to_ram_adress)

        self.cu_to_adding_ldi_ram_driver_in_a.set_input(self.control_unit.ldi_out_data)
        self.adding_ldi_ram_to_data_driver.input_a.set_input(self.cu_to_adding_ldi_ram_driver_in_a)

        self.adding_to_adding_ldi_ram_driver_in_b.set_input(self.adding_unit.output)
        self.adding_ldi_ram_to_data_driver.input_b.set_input(self.adding_to_adding_ldi_ram_driver_in_b)

        self.ram_to_adding_ldi_ram_in_c.set_input(self.ram.output)
        self.adding_ldi_ram_to_data_driver.input_c.set_input(self.ram_to_adding_ldi_ram_in_c)

        self.cu_to_adding_ldi_ram_driver_op_a.set_input(self.control_unit.adding_ldi_ram_driver_out_op_a)
        self.adding_ldi_ram_to_data_driver.input_driver_a.set_input(self.cu_to_adding_ldi_ram_driver_op_a)

        self.cu_to_adding_ldi_ram_driver_op_b.set_input(self.control_unit.adding_ldi_ram_driver_out_op_b)
        self.adding_ldi_ram_to_data_driver.input_driver_b.set_input(self.cu_to_adding_ldi_ram_driver_op_b)

        self.cu_to_adding_ldi_ram_driver_op_c.set_input(self.control_unit.adding_ldi_ram_driver_out_op_c)
        self.adding_ldi_ram_to_data_driver.input_driver_c.set_input(self.cu_to_adding_ldi_ram_driver_op_c)

        self.adding_ldi_ram_to_reg_demux.set_input(self.adding_ldi_ram_to_data_driver.output)
        self.reg_demultiplexer.input.set_input(self.adding_ldi_ram_to_reg_demux)