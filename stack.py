class Stack:
    def __init__(self):
        self.items = []  # Initializes the stack

    def push(self, item):
        self.items.append(item)  # Adds an item to the top of the stack

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # Removes the top item from the stack and returns it
        else:
            return None  # Optionally, raise an exception

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # Returns the top item without removing it
        else:
            return None  # Optionally, raise an exception

    def size(self):
        return len(self.items)  # Returns the number of items in the stack

    def is_empty(self):
        return len(self.items) == 0  # Helper method to check if the stack is empty

