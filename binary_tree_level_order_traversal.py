class Solution:
    # BFS + queue
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
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
