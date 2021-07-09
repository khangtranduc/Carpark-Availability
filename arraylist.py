import numpy as np

class arraylist:

    def __init__(self):
        self.data = np.empty((1500,), dtype=object)
        self.capacity = 1500
        self.size = 0

    def update(self, row):
        for r in row:
            self.add(r)

    def add(self, x):
        if self.size == self.capacity:
            self.capacity *= 2
            newdata = np.empty((self.capacity,), dtype=object)
            newdata[:self.size] = self.data
            self.data = newdata

        self.data[self.size] = x
        self.size += 1

    def finalize(self):
        data = self.data[:self.size]
        return np.reshape(data, newshape=(len(data)//4, 4))