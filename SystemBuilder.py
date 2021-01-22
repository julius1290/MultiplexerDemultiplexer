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
    cu_o_ram_adress: BusWire
    cu_to_ram_op: BusWire
    cu_to_adding_ldi_ram_driver_in_a: BusWire
    cu_to_adding_ldi_ram_driver_op_a: BusWire
    cu_to_adding_ldi_ram_driver_op_b: BusWire
    cu_to_adding_ldi_ram_driver_op_c: BusWire
    cu_to_adding_data: BusWire
    adding_ldi_ram_to_reg_demux: BusWire
    reg_demux_out_a_to_reg_a: BusWire
    red_demux_out_b_to_reg_b: BusWire
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
        self.cu_o_ram_adress = BusWire()
        self.cu_to_ram_op = BusWire()
        self.cu_to_adding_ldi_ram_driver_in_a = BusWire()
        self.cu_to_adding_ldi_ram_driver_op_a = BusWire()
        self.cu_to_adding_ldi_ram_driver_op_b = BusWire()
        self.cu_to_adding_ldi_ram_driver_op_c = BusWire()
        self.cu_to_adding_data = BusWire()
        self.adding_ldi_ram_to_reg_demux = BusWire()
        self.reg_demux_out_a_to_reg_a = BusWire()
        self.red_demux_out_b_to_reg_b = BusWire()
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

