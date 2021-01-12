from Storage.BasicRam import BasicRam
from Storage.BasicRom import BasicRom
from Base.BusWire import BusWire


ram = BasicRam(8, 8)
rom = BasicRom(10)
ram.store(111011001, (1, 1))
print(ram.storage)
wire1 = BusWire()
wire2 = BusWire()
wire3 = BusWire()
wire4 = BusWire()

wire2.set_input(wire1)
wire3.set_input(wire2)
wire1.set_data(1)
print(wire3.get_data())
wire2.set_input(wire4)
wire4.set_data(3)
print(wire3.get_data())
wire5 = BusWire()
wire1.set_input(wire5)
wire5.set_data(5)
print(wire1.get_data())