import collections


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = collections.deque([None] * capacity, capacity)
        self.times_written = 0

    @property
    def current(self):
        return len(self.storage)

    def append(self, item):
        if None in self.storage:
            self.storage.append(item)
        else:
            self.storage[self.times_written % self.capacity] = item

        self.times_written += 1

    def get(self):
        return [element for element in self.storage if element is not None]
