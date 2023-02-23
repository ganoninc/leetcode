from typing import Optional
from enum import Enum


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        resultList = ListNode()
        resultHead = resultList
        prevValue = -1
        subTotal = 0
        # currentState = 
        while head != None: 
            if head.val != 0:
                if prevValue == 0:
                    resultList.next = ListNode()
                    resultList = resultList.next
                subTotal += head.val
            else:
                if prevValue != 0 and prevValue != -1:
                    resultList.val = subTotal
                    subTotal = 0

            prevValue = head.val
            head = head.next

        return resultHead.next


solution = Solution()
# a = solution.mergeNodes(ListNode(0, ListNode(1, ListNode(2, ListNode(0)))))
b = solution.mergeNodes(ListNode(0, ListNode(3, ListNode(1, ListNode(0, ListNode(4, ListNode(5, ListNode(2, ListNode(0)))))))))
print("From Mel to Syd")