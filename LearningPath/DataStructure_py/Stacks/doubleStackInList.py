class DoubleStack:
    def __init__(self):
        self._doubleStack = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.countLeft = 0
        self.countRight = -1

    def pushL(self, item):
        if self.countLeft > 3:
            print("Stack is Full")
            return
        self._doubleStack.insert(self.countLeft, item)
        self.countLeft += 1

    def pushR(self, item):
        if self.countRight < -6:
            print("Stack is Full")
            return
        self._doubleStack.insert(self.countRight, item)
        self.countRight -= 1

    def popL(self):
        if self.countLeft == 0:
            print("Stack is Full")
            return
        self._doubleStack.pop(self.countLeft)
        self.countLeft -= 1

    def popR(self):
        if self.countRight == -1:
            print("Stack is Full")
            return
        self._doubleStack.pop(self.countRight)
        self.countRight += 1

    def isEmptyL(self):
        self.countLeft = 0

    def isEmptyR(self):
        self.countRight = -1

    def isFullL(self):
        if self.countLeft > 3:
            return "Stack is Full"

    def isFullR(self):
        if self.countRight < -5:
            return "Stack is Full"


s1 = DoubleStack()
s1.pushL(1)
s1.pushL(2)
s1.pushL(3)
s1.pushL(4)
print(s1.countLeft)
print(s1.isFullL())
s1.pushL(4)
s1.popL()
s1.popL()
s1.popL()
s1.popL()
s1.popL()

s2 = DoubleStack()
s2.pushR(1)
s2.pushR(2)
s2.pushR(3)
s2.pushR(4)
s2.pushR(5)
print(s2.countRight)
print(s2.isFullR())
s2.pushR(6)
s2.pushR(7)
s2.popR()
s2.popR()
s2.popR()
s2.popR()
s2.popR()
s2.popR()
s2.popR()
