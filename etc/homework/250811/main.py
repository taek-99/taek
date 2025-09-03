class Stack:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self. items = [None] * capacity
        self.top = -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, item):
        if self.is_full():
            raise IndexError("Stack is full")
        self.top += 1
        self.items[self.top] = item

    def is_empty(self):
        return self.top == -1

    def pop(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        item = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        return self.items[self.top]


stack = Stack(3)

