from typing import Optional 

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head: Optional[ListNode] = None
        self.tail: Optional[ListNode] = None

    def insert_at_end(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2
        
        if not temp1 and not temp2:
            return None
        if not temp1 or not temp2:
            return temp1 or temp2
        
        list_r = LinkedList()
        
        while temp1 and temp2:
            if temp1.val <= temp2.val:
                list_r.insert_at_end(temp1.val)
                temp1 = temp1.next
            else:
                list_r.insert_at_end(temp2.val)
                temp2 = temp2.next
        
        while temp1:
            list_r.insert_at_end(temp1.val)
            temp1 = temp1.next
            
        while temp2:
            list_r.insert_at_end(temp2.val)
            temp2 = temp2.next
            
        return list_r.head