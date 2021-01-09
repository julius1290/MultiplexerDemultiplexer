from Storage.BasicRam import BasicRam
from Storage.BasicRom import BasicRom
from Base.BusWire import BusWire


ram = BasicRam(8, 8)
ram.store(111011001)

wire1 = BusWire()
wire2 = BusWire()
wire3 = BusWire()

wire2.set_input(wire1.output)
wire3.set_input(wire2.output)
wire1.set_data(1)
print(wire2.get_data())

rom = BasicRom(10)
rom.add_instruction(0, "111011101")
wire1.set_input(rom.output_wire.output)
print(rom.storage)
rom.read_instruction(0)
print(wire3.get_data())
print(wire1.get_data())