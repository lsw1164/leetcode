# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = set()
        
        def dfs(node, k):
            if not node: return False
            target = k - node.val
            if target in s: return True
            s.add(node.val)
            return dfs(node.left, k) or dfs(node.right, k)
            
        return dfs(root, k)
        
