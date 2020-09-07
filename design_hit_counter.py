from collections import defaultdict
class HitCounter:


    def __init__(self):
        self.q = deque()
        self.length = 0

    def hit(self, timestamp: int) -> None:
        self.q.append(timestamp)
        self.length += 1


    def getHits(self, timestamp: int) -> int:
        while self.q and timestamp - self.q[0] >= 300:
            self.q.popleft()
            self.length -= 1
        return self.length



# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
