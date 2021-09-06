# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        max_avg = -float('inf')
        
        def dfs(node):
            if not node: return (0, 0)
            nonlocal max_avg
            l_sum, l_cnt = dfs(node.left)
            r_sum, r_cnt = dfs(node.right)
            tree_sum = l_sum + r_sum + node.val
            tree_len = l_cnt + r_cnt + 1
            max_avg = max(max_avg, tree_sum/tree_len)
            return (tree_sum, tree_len)
        
        dfs(root)
        return max_avg