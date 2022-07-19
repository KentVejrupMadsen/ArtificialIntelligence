from sigmoid import sigmoid


class Neuron:
    def __init__(self):
        self.input = 0

        self.weight = 0
        self.bias = 0

        self.output = 0

    def get_input(self):
        return self.input

    def get_output(self):
        return self.output

    def get_weight(self):
        return self.weight

    def get_bias(self):
        return self.bias

    def set_input(self, inp):
        self.input = inp

    def set_output(self, out):
        self.output = out

    def set_weight(self, weight):
        self.weight = weight

    def set_bias(self, bias):
        self.bias = bias