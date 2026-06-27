from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        current = head
        
        # 1. نحولوا الـ Linked List لمصفوفة عادية
        while current is not None:
            arr.append(current.val)
            current = current.next
            
        # 2. نقارنوا المصفوفة مع المقلوب تاعها في سطر واحد
        return arr == arr[::-1]