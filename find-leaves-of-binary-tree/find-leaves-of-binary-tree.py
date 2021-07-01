# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        output = []
        
        def dfs(node):
            if node is None: return 0
            
            l_depth = dfs(node.left)
            r_depth = dfs(node.right)    
            depth = max(l_depth, r_depth) + 1    
            
            idx = depth - 1
            while idx >= len(output):
                output.append([])
            output[idx].append(node.val)
            
            return depth
        
        dfs(root)
        
        return output