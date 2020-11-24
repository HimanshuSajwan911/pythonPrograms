class Stack():
    def __init__(self):
        self.items = []

    def push(self):
        self.items.append()

    def pop(self):
        self.items.pop()

    def is_empty(self):
        return self.items == []

    def get_stack(self):
        print(Stack(self))


s = Stack()
print(s.is_empty())
s.push("a")
print(s.get_stack())
