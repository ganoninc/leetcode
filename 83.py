# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previously_read_value = -101
        if head != None:
            result = ListNode()
            result_cursor = result
            result_cursor_minus_one = None
            while head != None:
                if head.val != previously_read_value:
                    result_cursor.val = head.val
                    previously_read_value = head.val
                    result_cursor_minus_one = result_cursor
                    result_cursor.next = ListNode()
                    result_cursor = result_cursor.next
                head = head.next       

            if result_cursor.val == 0:
                result_cursor_minus_one.next = None

            return result
        else:
            return None
        

solution = Solution()
print(solution.deleteDuplicates(ListNode(1, ListNode(1, ListNode(2)))))