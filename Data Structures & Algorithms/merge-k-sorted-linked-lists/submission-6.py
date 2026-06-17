from typing import List, Optional

# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Base Case: If the input list is empty, return None
        if not lists:
            return None
        
        # Keep merging pairs of lists until only one fully merged list remains
        while len(lists) > 1:
            merged_lists = []
            
            # Iterate through the lists pairs (stepping by 2)
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # If there's a second list in the pair, take it; otherwise, take None
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                
                # Merge the two sorted lists and add the result to our temporary array
                merged_lists.append(self.mergeTwoLists(l1, l2))
            
            # Overwrite the old lists with the newly merged, halved list array
            lists = merged_lists
            
        # The final remaining list at index 0 is the complete sorted linked list
        return lists[0]

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node acts as a safe placeholder for the head of the merged list
        dummy = ListNode(0)
        curr = dummy
        
        # Traverse both lists and link the smaller node to 'curr.next'
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
            
        # Append the remaining elements if one list is longer than the other
        curr.next = list1 if list1 else list2
        
        # Return the actual starting node of the merged list
        return dummy.next