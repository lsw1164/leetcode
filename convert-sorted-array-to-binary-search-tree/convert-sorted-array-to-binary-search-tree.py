# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        def arr_2_bst(nums, left, right):
            if left > right: return None
            mid = (left + right) >> 1
            new_node = TreeNode(nums[mid])
            new_node.left = arr_2_bst(nums, left, mid-1)
            new_node.right = arr_2_bst(nums, mid+1, right)
            return new_node
        
        return arr_2_bst(nums, 0, len(nums)-1)
        