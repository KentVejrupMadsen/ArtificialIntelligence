from sigmoid import sigmoid
from math import pow


class NeuronActivation:
    def __init__(self, b=1.0, threshold=1, v=0):
        self.bias = b

        self.rightThreshold = threshold
        self.leftThreshold = -threshold

        self.value = v

        pass

    def result(self):
        if self.value > self.rightThreshold:
            return 1

        if self.value < self.leftThreshold:
            return -1

        return 0

    def activate(self, x):
        self.value = sigmoid(x, moveY=-1, breath=2, depth=self.bias)
        return self.value

    def get_bias(self):
        return self.bias

    def get_right_threshold(self):
        return self.rightThreshold

    def get_left_threshold(self):
        return self.leftThreshold

    def set_bias(self, value):
        self.bias = value

    def set_right_threshold(self, value):
        self.rightThreshold = value

    def set_left_threshold(self, value):
        self.leftThreshold = value

    def get_value(self):
        return self.value

    def set_value(self, v):
        self.value = v


class Neuron:
    def __init__(self):
        self.input = 0
        self.weight = 0
        self.output = 0

        self.activator = NeuronActivation()

    def combine(self):
        return pow(self.input, 2.0) * self.weight

    def calculate(self):
        self.activator.activate(self.combine())
        self.output = self.activator.result()

    def get_input(self):
        return self.input

    def get_output(self):
        return self.output

    def get_weight(self):
        return self.weight

    def get_bias(self):
        return self.activator.get_bias()

    def set_input(self, inp):
        self.input = inp

    def set_output(self, out):
        self.output = out

    def set_weight(self, weight):
        self.weight = weight

    def set_bias(self, bias):
        self.activator.set_bias(bias)


