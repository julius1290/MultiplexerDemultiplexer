from Storage.BasicRam import BasicRam
from Storage.BasicRom import BasicRom
from Base.BusWire import BusWire


ram = BasicRam(8, 8)
rom = BasicRom(10)
ram.store(111011001)

wire1 = BusWire()
wire2 = BusWire()
wire3 = BusWire()
wire4 = BusWire()

wire1.set_input(rom.output_wire.output)
wire2.set_input(wire1.output)
wire3.set_input(wire2.output)
wire1.set_next(wire2)
wire2.set_next(wire3)
wire1.set_data(1)
print(wire2.get_data())

rom.add_instruction(0, "111011101")
rom.add_instruction(1,"Hello, World")
print(rom.storage)
rom.read_instruction(0)
print(wire3.get_data())
print(wire1.get_data())
wire2.set_input(wire4.output)
wire4.set_data(2)
rom.read_instruction(1)
print(wire3.get_data())
print(wire1.get_data())
wire1.set_input(rom.output_wire.output)
rom.read_instruction(1)
print(wire3.get_data())