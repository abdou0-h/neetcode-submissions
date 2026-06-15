from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next 

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        prev =  None 
        length = count = 0
        
        while temp != None:
            temp = temp.next
            length += 1
        
        if (length == n):
            new_head = head.next
            return new_head
        
        temp = head
        
        while temp != None and count < (length - n):
            prev = temp
            temp = temp.next
            count += 1
        
        prev.next = temp.next
        temp = prev = None
        
        return head
    
        