# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        
        def tree_2_str(tree):
            node_strs = []
            st = []
            st.append(tree)
            while len(st) > 0:
                node = st[-1]
                st.pop()
                if not node:
                    node_strs.append('#$')
                    continue
                st.append(node.left)
                st.append(node.right)
                node_strs.append(f"#{node.val}$")
            return "".join(node_strs)
        
        return tree_2_str(subRoot) in tree_2_str(root)
    