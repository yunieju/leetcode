class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_info = [0,0] #depth, parent
        y_info = [0,0] 
       
        def dfs(root, key, key_info, depth):
            if not root:
                return
            if root.right and root.right.val == key:
                key_info[0], key_info[1] = depth+ 1, root.val
                return
            
            if root.left and root.left.val == key:
                key_info[0], key_info[1] = depth + 1, root.val
                return
            dfs(root.right, key, key_info, depth + 1)
            dfs(root.left, key, key_info, depth + 1)
            return 
        
        dfs(root, x, x_info, 0)
        dfs(root, y, y_info, 0)
    
        return (x_info[0] == y_info[0]) and (x_info[1] != y_info[1])
            
