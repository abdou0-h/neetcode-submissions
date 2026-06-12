from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    
    while curr:
        next_node = curr.next  
        curr.next = prev       
        prev = curr
        curr = next_node
        
    return prev  

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    
    while list1 and list2:
        curr.next = list1
        list1 = list1.next
        curr = curr.next
        curr.next = list2
        list2 = list2.next
        curr = curr.next
    
    if list1:
        curr.next = list1
    elif list2:
        curr.next = list2
        
    return dummy.next

    
    
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next: return
        slow = fast = head 
        while slow and fast and fast.next:
            if not fast.next.next or not fast.next.next.next:
                prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        slow = reverseList(slow)
        new_head = mergeTwoLists(head, slow)
        head.next = new_head.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                        