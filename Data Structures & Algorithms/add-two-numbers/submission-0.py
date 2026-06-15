class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node to simplify the head management of the new list
        dummy = ListNode(0)
        curr = dummy
        borrow = 0
        
        # Loop continues if there are nodes left in either list, or if a carry (borrow) remains
        while l1 or l2 or borrow:
            # Extract values; default to 0 if the linked list has reached its end
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # Calculate the sum of values along with the incoming carry
            total = v1 + v2 + borrow
            borrow = total // 10        # Updates carry for the next iteration (1 if total > 9, else 0)
            val = total % 10            # Extracts the single digit to store in the current node
            
            # Create a new node with the calculated digit and append it to the list
            curr.next = ListNode(val)
            curr = curr.next
            
            # Advance the source pointers if the next nodes exist
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        # Return the actual head of the resulting list, skipping the dummy node
        return dummy.next
    
