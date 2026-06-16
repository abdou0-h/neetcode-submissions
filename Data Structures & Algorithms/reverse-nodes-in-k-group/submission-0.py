from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return None
        
        temp = head
        c = 0

        while temp != None and c < k:
            temp = temp.next
            c += 1

        if c < k:
            return head
            
        prev = None
        curr = head
        count = 0
        
        while curr and count < k:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            count += 1
        
        head.next = self.reverseKGroup(next_node, k)
        
        return prev