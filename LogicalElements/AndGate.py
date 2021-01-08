class AndGate:

    # Bitwise and gate for n number of inputs
    def calculate(self, inputs: tuple):
        inputs = list(inputs)
        output: any = inputs[0]
        bit_len = output.bit_length()
        inputs.pop(0)
        for value in inputs:
            output &= value
        return bin(output)[2:].zfill(bit_len)
