from Data.ControlUnit import ControlUnit
from LogicalElements.AndGate import AndGate
from Storage.BasicRam import BasicRam
from Storage.BasicRom import BasicRom
from Base.BusWire import BusWire
from Base.Clock import Clock
from Data.InstructionCounter import InstructionCounter

ram = BasicRam(8, 8)
rom = BasicRom(10)

rom.add_instruction(0, "0001234567890abc")
rom.add_instruction(1, "0000000000000001")
rom.add_instruction(2, "0010000000000000")

wirea = BusWire()
wireb = BusWire()

and_gate = AndGate()
and_gate.input.append(wirea)
and_gate.input.append(wireb)
wirea.set_data(int("1101", 2))
wireb.set_data(int("1011", 2))
and_gate.calculate()
print(and_gate.output.get_data())
wire6 = BusWire()

ic = InstructionCounter()
clock = Clock(1)
wire6.set_input(clock.output)
ic.input.set_input(wire6)
clock.add_notify(ic)
clock.add_notify(rom)
rom.input_wire.set_input(ic.output)
cu = ControlUnit()
cu.input_wire.set_input(rom.output_wire)
clock.add_notify(cu)
ic.data_input.set_input(cu.ic_output)
ic.op_input.set_input(cu.op_output)
cu.initOuts()
clock.run()
