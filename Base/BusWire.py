from Base.Data import Data


class BusWire:

    input: Data
    output: Data

    def __init__(self):
        self.input = self. output = Data()

    def set_data(self, data: any):
        self.input.data = data

    def get_data(self):
        return self.output.data

    def set_input(self, input: Data):
        self.input = self.output = input
