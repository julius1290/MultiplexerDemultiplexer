from Base.Data import Data


class BusWire:

    input: Data
    output: Data
    next: any = None

    def __init__(self):
        self.input = self. output = Data()

    def set_data(self, data: any):
        self.input.data = data

    def get_data(self):
        return self.output.data

    def set_input(self, input: Data):
        self.input = self.output = input
        if self.next is not None:
            self.next.set_input(self.output)

    def set_next(self, next: any):
        self.next = next
