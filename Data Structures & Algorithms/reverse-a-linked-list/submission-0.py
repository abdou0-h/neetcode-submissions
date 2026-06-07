# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next  # 1. نخبو الـ Node الجاية قبل ما نقطعوا الخيط
            curr.next = prev       # 2. السحر هنا: نقلبوا السهم يشوف للور (للـ prev)
            
            # 3. ندنيو الـ Pointers للقدام باش نروحوا للعنصر القادم
            prev = curr
            curr = next_node
            
        return prev  # في النهاية الـ prev هو اللي راح يكون الـ head الجديد