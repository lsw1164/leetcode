# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.order = []
        self.idx = -1
        
        def dfs(node):
            if not node: return
            dfs(node.left)
            self.order.append(node)
            dfs(node.right)
            
        dfs(root)
        

    def next(self) -> int:
        self.idx += 1
        return self.order[self.idx].val
        

    def hasNext(self) -> bool:
        return self.idx + 1 < len(self.order)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()