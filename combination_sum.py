class Solution:
    def dfs(self, candidates, target, index, res, path):
        if target < 0:
            return
        
        if target == 0:
            res.append(path)
            return
    
        for i in range(index, len(candidates)):
            self.dfs(candidates, target - candidates[i], i, res, path + [candidates[i]]) 
            
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()
        self.dfs(candidates, target, 0, res, path)
        return res
    
