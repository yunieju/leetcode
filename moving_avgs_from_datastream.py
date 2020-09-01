class MovingAverage:

    def __init__(self, size: int):
        self.q = [0] * size
        self.size = size
        self.idx = 0
        self.count = 0


    def next(self, val: int) -> float:
        self.q[self.idx] = val
        self.idx = (self.idx + 1) % self.size
        self.count += 1
        if self.count < self.size:
            return sum(self.q)/ self.count
        return sum(self.q) / self.size




# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
