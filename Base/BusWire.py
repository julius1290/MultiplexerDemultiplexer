from Base.Data import Data


class BusWire:

    input: Data
    output: Data
    next: []
    before: any

    def __init__(self):
        self.input = self. output = Data()
        self.next = []
        self.before = None

    def set_data(self, data: any):
        self.input.data = data

    def get_data(self):
        return self.output.data

    def set_input(self, wire: any):
        self.input = self.output = wire.input
        if self.before is not None:
            self.before.next.remove(self)
        wire.next.insert(0, self)
        self.before = wire
        for elem in self.next:
            elem.set_input(self)

    def set_next(self, next: any):
        self.next = next
