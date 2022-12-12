class IterateContent:
    def __init__(self):
        self.lines = None
        self.index = 0

    def next(self):
        self.set_index(self.get_index() + 1)

    def previous(self):
        self.set_index(self.get_index() - 1)

    def get_line(self):
        return self.lines[self.get_index()]

    def get_index(self):
        return self.index

    def set_index(self, value):
        self.index = value

    def get_lines(self):
        return self.lines

    def set_lines(self, arr):
        if isinstance(arr, list):
            self.lines = arr



