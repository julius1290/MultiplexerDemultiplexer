from Base.Data import Data


class BusWire:

    input: Data
    output: Data
    next: any = None
    before: any = None

    def __init__(self):
        self.input = self. output = Data()

    def set_data(self, data: any):
        self.input.data = data

    def get_data(self):
        return self.output.data

    def set_input(self, wire: any):
        self.input = self.output = wire.input
        if self.before is not None:
            self.before.next = None
        wire.next = self
        self.before = wire
        if self.next is not None:
            self.next.set_input(self)

    def set_next(self, next: any):
        self.next = next
