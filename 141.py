# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Version 1 using a hashmap
    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     if head == None:
    #         return False
        
    #     visitedNodes = {}
    #     while head.next != None:
    #         if head in visitedNodes:
    #             return True
    #         else:
    #             visitedNodes[head] = head.val
    #             head = head.next

    #     return False


    # Version 2, with O(1) memory, kinda bruteforce
    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     if head == None:
    #         return False
        
    #     node_count = 0
    #     max_node_count = pow(10, 4)
    #     while head.next != None and node_count <= max_node_count:
    #         head = head.next
    #         node_count = node_count + 1

    #     if node_count > max_node_count:
    #         return True
        
    #     return False


    # Version 3, with two pointers
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        
        fast = head
        slow = head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True
        
        return False
        
