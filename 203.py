# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:

    def cleanListNode(self, cleaned_list_node, head, val) -> ListNode:
        if head.val == val:
            if head.next != None:
                self.cleanListNode(cleaned_list_node, head.next, val)
        
        else:
            cleaned_list_node.next = ListNode(head.val)
            cleaned_list_node = cleaned_list_node.next
            if head.next != None:
                self.cleanListNode(cleaned_list_node, head.next, val)
        

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return None

        cleaned_list_node = ListNode()
        cleaned_list_head = cleaned_list_node

        self.cleanListNode(cleaned_list_node, head, val)
            
        if head == None:
            return None
        else:
            if cleaned_list_head.next != None:
                return cleaned_list_head.next
            else:
                return None
        
solution = Solution()
# dirty_list = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))
dirty_list = ListNode(1)
# dirty_list = ListNode(1, ListNode(1, ListNode(2)))
cleaned_list = solution.removeElements(dirty_list, 1)
print(cleaned_list)