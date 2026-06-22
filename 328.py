# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        if not head.next:
            return head
        
        odd_head = ListNode()
        odd_curr = odd_head
        even_head = ListNode()
        even_curr = even_head

        curr = head
        i = 1

        while curr != None:
            if i % 2 == 0:
                even_curr.next = curr
                even_curr = even_curr.next
            else:
                odd_curr.next = curr
                odd_curr = odd_curr.next

            i += 1
            curr = curr.next

        odd_curr.next = even_head.next
        even_curr.next = None

        return odd_head.next