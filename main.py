from Storage.BasicRam import BasicRam
from Storage.BasicRom import BasicRom
from Base.BusWire import BusWire
from Base.Clock import Clock
from Data.InstructionCounter import InstructionCounter

ram = BasicRam(8, 8)
rom = BasicRom(10)

rom.add_instruction(0, "111023")
wire1 = BusWire()
wire2 = BusWire()
wire3 = BusWire()
wire4 = BusWire()


wire6 = BusWire()

ic = InstructionCounter()
clock = Clock(1)
wire6.set_input(clock.output)
ic.input.set_input(wire6)
clock.add_notify(ic)
clock.add_notify(rom)
rom.input_wire.set_input(ic.output)
clock.run()