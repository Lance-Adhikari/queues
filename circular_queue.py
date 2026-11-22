class CircularQueue:
    def __init__(self, size):
        self.array = [None] * size
        self.size = size
        self.read = 0
        self.write = 0

    def enqueue(self, key):
        # Wrap around to reuse positions at the start of the array.
        next_write = (self.write + 1) % self.size

        # Leave one slot unused to distinguish a full queue from an empty one.
        if next_write == self.read:
            print("Queue is full")
            return

        self.array[self.write] = key
        self.write = next_write

    def dequeue(self):
        if self.read == self.write:
            print("Queue is empty")
            return None

        value = self.array[self.read]
        self.array[self.read] = None

        self.read = (self.read + 1) % self.size
        return value

    def empty(self):
        return self.read == self.write


q = CircularQueue(5)

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

print(q.dequeue())
print(q.dequeue())

q.enqueue("D")
q.enqueue("E")
q.enqueue("F")

print(q.array)
print(q.empty())
