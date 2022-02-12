# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        dq = deque()
        dq.append(root.left)
        dq.append(root.right)
        
        while len(dq) > 0:
            l = dq.popleft()
            r = dq.popleft()
            if l == None and r == None: continue
            elif l == None and r != None: return False
            elif l != None and r == None: return False
            elif l.val != r.val: return False
            
            dq.append(l.left)
            dq.append(r.right)
            
            dq.append(l.right)
            dq.append(r.left)
            
        return True
        