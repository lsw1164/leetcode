# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def get_len(self, head):
        cur = head
        cnt = 0
        while cur: 
            cur = cur.next
            cnt += 1
        return cnt
        
        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list_len = self.get_len(head)
        
        if list_len <= 1: 
            return True
        
        prev, right = None, head
        
        for _ in range(list_len >> 1):
            next_node = right.next
            right.next = prev
            prev = right
            right = next_node
            
        left = prev
        if list_len % 2 != 0:
            right = right.next
            
        while right:
            if left.val != right.val: return False
            
            left = left.next
            right = right.next
            
        return True
        