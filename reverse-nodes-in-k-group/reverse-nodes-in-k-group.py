# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def get_len(self, head: ListNode):
        cnt = 0
        while head:
            cnt += 1 
            head = head.next
        return cnt
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        p_node, c_node, n_node = None, head, head.next
        p_last, first, last = None, None, None
        length = self.get_len(head)
        
        new_head = None
        
        for i in range(length - length % k):
            c_node.next = p_node
            
            if i % k == 0: 
                p_last = last
                last = c_node
            if i % k == k - 1:
                first = c_node
                if not new_head: new_head = first
                if p_last: p_last.next = first
                last.next = n_node
                
            p_node = c_node
            c_node = n_node
            if n_node: n_node = n_node.next
            
        if not new_head: new_head = head 
        return new_head