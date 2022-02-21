# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root == None: return 0
        
        hash_map = {}
        cnt = 0
        
        def dfs(node, prev_path_sum):
            nonlocal cnt, hash_map
            if node == None: return
            
            cur_path_sum = prev_path_sum + node.val
            prev_seen = cur_path_sum - targetSum
            
            if cur_path_sum == targetSum:
                cnt += 1
                
            if hash_map.get(prev_seen, 0) > 0:
                cnt += hash_map.get(prev_seen, 0)
                
            hash_map[cur_path_sum] = hash_map.get(cur_path_sum, 0) + 1
            
            dfs(node.left, cur_path_sum)
            dfs(node.right, cur_path_sum)
            
            hash_map[cur_path_sum] = max(0, hash_map.get(cur_path_sum, 0) - 1)
            
        dfs(root, 0)
        return cnt