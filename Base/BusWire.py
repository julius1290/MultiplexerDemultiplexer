from Base.Input import Input
from Base.Output import Output


class BusWire:
    input: Input = Input
    output: Output = Output

    def set_data(self, data: any):
        self.input.data = data
        self.output.data = self.input.data
