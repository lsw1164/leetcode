# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        
        def dfs(node, cur_sum, cur_path):
            if not node:
                return
            
            cur_sum += node.val
            cur_path.append(node.val)
            
            if node.left == None and node.right == None:
                if cur_sum == targetSum:
                    ans.append(cur_path.copy())
            
            dfs(node.left, cur_sum, cur_path)
            dfs(node.right, cur_sum, cur_path)
            
            cur_path.pop()
            
            
        dfs(root, 0, [])
        
        return ans