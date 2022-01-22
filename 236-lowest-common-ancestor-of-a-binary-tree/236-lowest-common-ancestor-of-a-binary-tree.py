# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
        
    def get_parent_hash_map(self, root):
        parent_map = {}
        
        def dfs(node, parent):
            if node == None: return
            parent_map[node.val] = parent
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root, None)
        return parent_map 
            
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q: return root
        
        parent_map = self.get_parent_hash_map(root)
        
        visit = {}
        while p:
            visit[p.val] = True
            p = parent_map[p.val]
        while q:
            if q.val in visit and visit[q.val]: return q
            q = parent_map[q.val]
        
        return root
            
        