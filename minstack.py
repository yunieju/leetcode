class MinStack:

    def __init__(self):
        self.stack = []
        self.min = 999999
        

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(x)
            self.min = x
            return
        else:
            if x < self.min:
                self.min = x
            self.stack.append(x)

    def pop(self) -> None:
        i = self.stack.pop()
        if i == self.min and len(self.stack) != 0:
            self.min = min(self.stack)
    
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
