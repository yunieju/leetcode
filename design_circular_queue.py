class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.head = -1
        self.tail = -1
        self.queue = [0] * k
        self.cap = k


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        if self.tail == -1:
            self.tail = self.head = 0
        else:
            self.head = (self.head + 1) % self.cap
        self.size -= 1
        return True


    def enQueue(self, value):
        if self.isFull(): return False
        else:
            if self.tail == -1:
                self.tail = self.head = 0
            else:
                self.tail = (self.tail + 1)%self.cap
            self.queue[self.tail] = value
            self.size += 1
            return True


    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]


    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail]


    def isEmpty(self) -> bool:
        return self.size == 0


    def isFull(self) -> bool:
        return self.size == self.cap



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
