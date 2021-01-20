from Data.ControlUnit import ControlUnit
from LogicalElements.AndGate import AndGate
from LogicalElements.NotGate import NotGate
from LogicalElements.OrGate import OrGate
from Storage.BasicRam import BasicRam
from Storage.BasicRom import BasicRom
from Base.BusWire import BusWire
from Base.Clock import Clock
from Data.InstructionCounter import InstructionCounter
from Multiplexer.Multiplexer import ToWireMultiplexer
from Multiplexer.FourWireMultiplexer import FourWireMultiplexer

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
wirea.set_data("1101")
wireb.set_data("1001")
and_gate.calculate()
print(and_gate.output.get_data())
wire6 = BusWire()

or_gate = OrGate()
or_gate.input.append(wirea)
or_gate.input.append(wireb)
or_gate.calculate()
print(or_gate.output.get_data())

not_gate = NotGate()
not_gate.input.set_input(wirea)
not_gate.calculate()
print(not_gate.output.get_data())








wire_one = BusWire()
wire_two = BusWire()
wire_three = BusWire()
wire_four = BusWire()

mux = ToWireMultiplexer()
mux.input_a.set_input(wire_one)
mux.input_b.set_input(wire_two)
mux.input_c.set_input(wire_three)
wire_four.set_input(mux.output)
wire_one.set_data("00000001")
wire_two.set_data("00000101")
wire_three.set_data("11111111")
mux.notify()
print("Mux_out:")
print(wire_four.get_data())
wire_three.set_data("0")
mux.notify()
print(wire_four.get_data())
wire_three.set_data("111111111")
mux.notify()
print(wire_four.get_data())

wire = BusWire()
wiree = BusWire()
wireee = BusWire()
wireeee = BusWire()
wiree.set_input(wire)
wireee.set_input(wire)
wireeee.set_input(wire)
wire.set_data("e")
print(wireeee.get_data())

print("mux4test")
wire1 = BusWire()
wire2 = BusWire()
wire3 = BusWire()
wire4 = BusWire()
wire5 = BusWire()
wire6 = BusWire()
wire7 = BusWire()

mux4 = FourWireMultiplexer()
mux4.input_a.set_input(wire1)
mux4.input_b.set_input(wire2)
mux4.input_c.set_input(wire3)
mux4.input_d.set_input(wire4)
mux4.op_a.set_input(wire5)
mux4.op_b.set_input(wire6)
wire7.set_input(mux4.output)

wire1.set_data("00000011")
wire2.set_data("00001100")
wire3.set_data("00110000")
wire4.set_data("11000000")
wire5.set_data("11111111")
wire6.set_data("00000000")
mux4.notify()
print(wire7.get_data())
wire5.set_data("00000000")
mux4.notify()
print(wire7.get_data())
wire6.set_data("11111111")
mux4.notify()
print(wire7.get_data())
wire5.set_data("11111111")
mux4.notify()
print(wire7.get_data())
















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
