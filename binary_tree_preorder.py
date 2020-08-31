#recursive + dfs
def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res

#iterative
def preorderTraversal(self, root: TreeNode) -> List[int]:
    res = []
    stack = [root]

    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return res
