# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node: return (0, 0)
            l_rob, l_not_rob = dfs(node.left)
            r_rob, r_not_rob = dfs(node.right)
            rob = node.val + l_not_rob + r_not_rob
            not_rob = max(l_rob, l_not_rob) + max(r_rob, r_not_rob)
            return (rob, not_rob)
        
        rob, not_rob = dfs(root)
        
        return max(rob, not_rob)
        