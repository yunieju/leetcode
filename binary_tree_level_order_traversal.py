class Solution:
    # BFS + queue
   class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        q = [(root,0)]
        while q:
            curr,depth = q.pop()
            if curr:
                q.append((curr.right, depth + 1))
                q.append((curr.left, depth + 1))
            
                if len(res) <= depth:
                    res.append([curr.val])
                else:
                    res[depth].append(curr.val)
            
        
        return res
    
    # DFS recursively
    def levelOrderBottom2(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.dfs(0, root, res)
                    
        return res
    def dfs(self, level: int, root: TreeNode, res)-> List[List[int]]:
        if root:
            if len(res) < level + 1:
                res.insert(0, [])
            res[-(level+1)].append(root.val)
            self.dfs(level +1, root.left, res)
            self.dfs(level +1, root.right, res)
