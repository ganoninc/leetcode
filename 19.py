# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def countNodes(self, node, deepIndex):
        if node.next == None:
            return deepIndex
        
        else:
            return self.countNodes(node.next, deepIndex+1)

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None

        noode_list_size = self.countNodes(head, 1)
        node_to_be_deleted = noode_list_size - n
        i = 0
        node = head
        prev_node = None
        while i <= node_to_be_deleted:
            if i == node_to_be_deleted:
                if i == 0:
                    head = head.next
                    break
                else :
                    prev_node.next = node.next
                    break
            i += 1
            prev_node = node
            node = node.next

        return head


solution = Solution()
solution.removeNthFromEnd(ListNode(5, ListNode(6, ListNode(2, ListNode(3, ListNode(9))))), 2)
# solution.removeNthFromEnd(ListNode(1, ListNode(2)), 2)