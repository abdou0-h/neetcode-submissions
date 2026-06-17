from typing import Optional
from typing import List

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
        
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
        
    if list1:
        curr.next = list1
    elif list2:
        curr.next = list2
        
    return dummy.next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        
        if not lists or not lists[0]:
            return dummy.next
        
        for i in range(len(lists)):
            curr.next = mergeTwoLists(curr.next, lists[i])
        
        return dummy.next