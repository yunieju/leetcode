class Solution:
    # BFS + queue
    def levelOrderBottom1(self, root: TreeNode) -> List[List[int]]:
        q = [(0,root)]
        res = []
        while q:
            i, node = q.pop(0)
            if node:
                if node.left:
                    q.append((i+1, node.left))
                if node.right:
                    q.append((i+1, node.right))
                if len(res) < i+1:
                    res.insert(0, [])
                res[-(i+1)].append(node.val)
                    
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