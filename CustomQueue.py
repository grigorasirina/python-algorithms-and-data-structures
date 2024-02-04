# Define the CustomQueue class to implement a queue data structure
class CustomQueue:
    def __init__(self):
        """Initialize an empty queue."""
        self.items = []

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item at the front of the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue.")
        return self.items.pop(0)

    def peek(self):
        """Return the item at the front of the queue without removing it."""
        if self.is_empty():
            raise IndexError("Peek from an empty queue.")
        return self.items[0]

    def is_empty(self):
        """Return True if the queue is empty, otherwise False."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)

    def __len__(self):
        """Enable the use of the len() function to get the size of the queue."""
        return self.size()

    def __str__(self):
        """Return a string representation of the queue."""
        return f"CustomQueue({self.items})"

    def __iter__(self):
        """Provide an iterator to allow iterating through the queue from front to end."""
        return iter(self.items)

# Example usage of the CustomQueue class
if __name__ == "__main__":
    cq = CustomQueue()
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    print(f"Queue after enqueues: {cq}")
    print(f"Front item (peek): {cq.peek()}")
    dequeued_item = cq.dequeue()
    print(f"Dequeued item: {dequeued_item}")
    print(f"Queue after dequeue: {cq}")
    print(f"Queue size: {len(cq)}")

