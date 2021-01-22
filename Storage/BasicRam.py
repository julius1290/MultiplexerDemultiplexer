from Base.BusWire import BusWire


class BasicRam:

    pages: int
    rows: int
    storage: any
    input: BusWire
    output: BusWire
    opcode: BusWire
    address: BusWire

    def __init__(self, pages: int, rows: int):
        self.storage = [[None for x in range(rows)] for y in range(pages)]
        self.pages = pages
        self.rows = rows
        self.input = BusWire()
        self.address = BusWire()
        self.opcode = BusWire()
        self.output = BusWire()

    def store(self):
        store_address = int(self.address.get_data(), 2)
        page = store_address//8
        row = store_address % 8
        if self.storage[page][row] is None:
            self.storage[page][row] = self.input.get_data()
            return (page, row)
        print("RamOverload")
        return (-1, -1)

    def read(self):
        store_address = int(self.address.get_data(), 2)
        page = store_address // 8
        row = store_address % 8
        self.output.set_data(self.storage[page][row])
        return self.storage[page][row]

    def delete(self):
        store_address = int(self.address.get_data(), 2)
        page = store_address // 8
        row = store_address % 8
        self.storage[page][row] = None

    def notify(self):
        op = self.opcode.get_data()
        if op == "10":
            self.store()
        if op == "11":
            self.read()
