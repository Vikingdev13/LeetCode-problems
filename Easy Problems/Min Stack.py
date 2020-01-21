class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min.append(min(self.min[-1], x)) if self.min else self.min.append(x)

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.stack)
param3 = obj.top()
param4 = obj.getMin()
obj.push(-13)
print(obj.stack)
print(obj.top())
print(obj.getMin())
obj.pop()
print(obj.stack)
print(obj.top())
print(obj.getMin())
obj.pop()
print(obj.stack)
print(obj.top())
print(obj.getMin())