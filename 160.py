# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited_nodes = {}
        head_a_pointer = headA
        head_b_pointer = headB

        while head_a_pointer != None:
            visited_nodes[head_a_pointer] = head_a_pointer.val
            head_a_pointer = head_a_pointer.next

        while head_b_pointer != None:
            if head_b_pointer in visited_nodes:
                return head_b_pointer
            head_b_pointer = head_b_pointer.next
            
        return None