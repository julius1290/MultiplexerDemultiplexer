from Storage.BasicRam import BasicRam
from Base.BusWire import BusWire


ram = BasicRam(8, 8)
ram.store(111011001)

wire1 = BusWire
wire2 = BusWire
wire3 = BusWire

wire2.input = wire1.output
wire3.input = wire2.output
wire1.input.data = 1
print(wire3.output.data)