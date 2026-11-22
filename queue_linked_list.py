class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, key):
        new_node = Node(key)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # Add new values at the tail.
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None

        # Remove the oldest value from the head.
        value = self.head.key
        self.head = self.head.next

        # Clear the tail when the last node is removed.
        if self.head is None:
            self.tail = None

        return value

    def empty(self):
        return self.head is None


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())
print(q.dequeue())
print(q.empty())
