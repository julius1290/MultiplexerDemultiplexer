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

    def store(self, data_word):
        for i in range(self.pages):
            for j in range(self.rows):
                if self.storage[i][j] is None:
                    self.storage[i][j] = self.input.get_data()
                    return (i,j)
        print("RamOverload")
        return (-1, -1)

    def read(self, page: int, row: int):

        self.output.set_data(self.storage[page][row])
        return self.storage[page][row]

    def delete(self, page: int, row: int):
        self.storage[page][row] = None

    def notifiy(self):
        op = self.opcode.get_data()
        if op is "1101":
            self.store()
        if op is "1110":
            self.read()
