# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_two_lists = ListNode()
        merged_two_lists_current_cursor = merged_two_lists

        if list1 == None and list2 == None:
            return None

        while list1 != None or list2 != None:
            if list1 == None:
                merged_two_lists_current_cursor.val = list2.val
                list2 = list2.next
                if list2 != None:
                    merged_two_lists_current_cursor.next = ListNode()
                merged_two_lists_current_cursor = merged_two_lists_current_cursor.next

            elif list2 == None:
                merged_two_lists_current_cursor.val = list1.val
                list1 = list1.next
                if list1 != None:
                    merged_two_lists_current_cursor.next = ListNode()
                merged_two_lists_current_cursor = merged_two_lists_current_cursor.next
            
            else:
                if list1.val <= list2.val:
                    merged_two_lists_current_cursor.val = list1.val
                    list1 = list1.next
                    if list1 != None or list2 != None:
                        merged_two_lists_current_cursor.next = ListNode()
                    merged_two_lists_current_cursor = merged_two_lists_current_cursor.next
                    
                else :
                    merged_two_lists_current_cursor.val = list2.val
                    list2 = list2.next
                    if list1 != None or list2 != None:
                        merged_two_lists_current_cursor.next = ListNode()
                    merged_two_lists_current_cursor = merged_two_lists_current_cursor.next
                

        return merged_two_lists
        
list_a = ListNode(-9, ListNode(3))
list_b = ListNode(5, ListNode(7))
solution = Solution()
print(solution.mergeTwoLists(list_a, list_b))