from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: 
            return
        
        # 1. إيجاد المنتصف (بلا شروط معقدة لداخل)
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 2. تقطيع اللستة على زوج
        second = slow.next
        slow.next = None  # هنا قطعنا اللستة الأولى
        
        # 3. قلب النصف الثاني (In-place ديريكت بلا دالة خارجية)
        prev = None
        curr = second
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # درك: head هو بداية النص الأول، و prev هو بداية النص الثاني المقلوب
        
        # 4. الدمج الذكي بالتناوب (أسرع وخفيف عالميموري)
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            
            first.next = second  # نربطو الأول مع تاع النص الثاني
            second.next = tmp1   # نربطو تاع النص الثاني مع التالي تاع النص الأول
            
            first, second = tmp1, tmp2 # نـقدّمو البوانتورات