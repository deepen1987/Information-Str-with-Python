class Stack:
    def __init__(self):
        self._myStack = []

    def __str__(self):
        return str(self._myStack)

    def push(self, item):
        self._myStack.append(item)

    def pop(self):
        return self._myStack.pop()

    def peek(self):
        return self._myStack[-1]

    def isEmpty(self):
        return len(self._myStack) == 0


s = Stack()
s.push(1)
print(s.peek())
s.push(2)
s.push(3)
print(s.peek())
s.pop()
print(s)

