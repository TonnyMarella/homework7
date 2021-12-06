class Stack:
    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)

    def pop(self):
        if len(self.values) == 0:
            print(f"Empty Stack")
        else:
            d = self.values[-1]
            self.values = self.values[0:-1]
            return d

    def peek(self):
        if len(self.values) == 0:
            print(f"Empty Stack")
            return None
        else:
            return self.values[-1]

    def is_empty(self):
        if len(self.values) == 0:
            return True
        else:
            return False


s = Stack()
s.peek()
print(s.is_empty())
s.push('cat')
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.is_empty())
s.push(777)
print(s.pop())
print(s.pop())
print(s.size())