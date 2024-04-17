class LinkedList:
    def remove_from_head(self):
        if self.head is not None:
            h = self.head
            if self.head.next is None:
                self.head = None
                self.tail = None
                return h
            self.head = self.head.next            
            if self.head.next is None:
                self.tail = self.head
            return h
        return None
    
    def add_to_head(self, node):
        if self.head:
            node.set_next(self.head)
            self.head = node
        self.head = node

    def add_to_tail(self, node):
        if self.head:
            for s_node in self:
                last_node = s_node
            last_node.next = node
        else:
            self.head = node
    
    def add_to_head_q(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        node.set_next(self.head)
        self.head = node

    def add_to_tail_q(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node

    
    def __init__(self):
        self.head = None

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    # don't touch below this line

    def __repr__(self):
        return self.val
