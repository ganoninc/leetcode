# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    head_of_reversed_list = None

    def reverseListRecursive(self, head) -> ListNode:
        if head.next == None:
            self.head_of_reversed_list = ListNode(head.val)
            return self.head_of_reversed_list

        else:
            nextElt = self.reverseListRecursive(head.next)
            nextElt.next = ListNode(head.val)
            return nextElt.next

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        if head.next == None:
            return head

        self.reverseListRecursive(head)

        return self.head_of_reversed_list


        
solution = Solution()
a_list = ListNode(1, ListNode(2, ListNode(3)))
a_reversed_list = solution.reverseList(a_list)
print(a_list)