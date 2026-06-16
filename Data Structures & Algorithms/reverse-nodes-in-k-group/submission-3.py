from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return None

        check = head
        for _ in range(k):
            if not check: return head
            check = check.next
            
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