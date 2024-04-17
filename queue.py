class Queue:
    def __init__(self):
        self.items = []  # Initializes the queue

    def push(self, item):
        self.items.append(item)  # Enqueues an item to the back of the queue

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)  # Dequeues the item from the front of the queue and returns it
        else:
            return None  # Optionally, raise an exception

    def peek(self):
        if not self.is_empty():
            return self.items[0]  # Returns the item at the front of the queue without removing it
        else:
            return None  # Optionally, raise an exception

    def size(self):
        return len(self.items)  # Returns the number of items in the queue

    def is_empty(self):
        return len(self.items) == 0  # Helper method to check if the queue is empty
