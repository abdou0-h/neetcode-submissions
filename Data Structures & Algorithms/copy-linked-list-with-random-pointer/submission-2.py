from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def insert_at_end(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
        
        
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_list = LinkedList()
        temp = head
        Dic1 = {}
        Dic2 = {}
        index = 0
        
        while temp != None:
            new_list.insert_at_end(temp.val)
            temp2 = new_list.tail
            Dic1[index] = temp.random
            Dic2[temp]  = temp2
            index += 1
            temp = temp.next

        temp = new_list.head
        i = 0

        while temp != None:
            # Retrieve the Node reference instantly in O(1) time complexity
            retrieved_node = Dic1[i]
            key = retrieved_node
            if key in Dic2:
                temp.random = Dic2[key]
            else:
                temp.random = None
            i += 1
            temp = temp.next
            
        return new_list.head
                    

        