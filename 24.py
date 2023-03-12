# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def swapNode(self, node, prevNode):
        if node.next != None:
            nodeA = node
            prevNode.next = node.next
            nodeA.next = node.next.next
            prevNode.next.next = nodeA
            if nodeA.next != None and nodeA.next.next != None:
                self.swapNode(node.next, node)

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        if head.next == None:
            return head

        formerHead = head
        head = head.next
        formerHead.next = head.next
        head.next = formerHead

        if formerHead.next != None and formerHead.next.next != None:
            self.swapNode(formerHead.next, formerHead)

        return head

        


solution = Solution()
solution.swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
