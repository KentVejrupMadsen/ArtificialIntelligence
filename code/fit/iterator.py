class Iterator:
    def __init__(self):
        self.currentPos = 0
        self.size = 0

    def next(self):
        self.move(1)

    def move(self, to):
        self.currentPos = self.currentPos + to

    def continue_iterating(self):
        return self.currentPos < self.size

    def get_current_position(self):
        return self.currentPos

    def set_current_position(self, value):
        self.currentPos = value

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size