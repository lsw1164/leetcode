# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        st = []
        
        def get_sum(node):
            if not node: return 0
            root_sum = get_sum(node.left) + get_sum(node.right) + node.val
            st.append(root_sum)
            return root_sum
        
        total = get_sum(root)
        st.pop()
        
        return total % 2 == 0 and total // 2 in st
    
        