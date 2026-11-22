# Queues

Two Python examples of a queue, where the first value added is the first removed.

- [queue_linked_list.py](queue_linked_list.py): Adds nodes at the tail and removes them from the head. Removing from an empty queue returns `None`.
- [circular_queue.py](circular_queue.py): Uses an array with read and write positions that wrap around. One slot stays unused, so an array of size 5 holds 4 values. Use a size of at least 2. Full and empty operations print a message.

Both files run independently and print their example results.
