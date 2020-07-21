class Solution:
    def convertToTitle(self, n: int) -> str:
        arr = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        res = []
        while n > 0:
            n, r = divmod(n-1, 26)
            res.append(arr[r])
        
        return "".join(res[::-1])
