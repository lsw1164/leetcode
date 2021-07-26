# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        root = TreeNode()
        
        def add(num):
            new_node = TreeNode(num)
            cur = root
            while cur:
                if num < cur.val:
                    if cur.left: 
                        cur = cur.left
                        continue
                    cur.left = new_node
                    break
                else:
                    if cur.right:
                        cur = cur.right
                        continue
                    cur.right = new_node
                    break
        
        def arr2bst(left, right):
            if left > right: return
            mid = (left + right) >> 1
            add(nums[mid])
            arr2bst(left, mid-1)
            arr2bst(mid+1, right)
        
        left, right = 0, len(nums)-1
        mid = (left + right) >> 1
        root.val = nums[mid]
        arr2bst(left, mid-1)
        arr2bst(mid+1, right)
        return root
        