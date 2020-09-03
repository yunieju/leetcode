class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = [("0000", 0)]
        visited = set()
        count = 0
        while len(q) > 0:
            cur, count = q.pop(0)
            if cur == target:
                return count
            if cur in deadends:
                continue
            visited.add(cur)

            for n in self.neighbors(cur):
                if n not in visited:
                    visited.add(n)
                    q.append((n, count + 1))
        return -1



    def neighbors(self, num: str):
        for i in range(4):
                x = int(num[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield num[:i] + str(y) + num[i+1:]




        
