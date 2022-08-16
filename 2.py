import numbers
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def parseIntFromReversedLinkedList(self, reversedLinkedList:ListNode) -> int:
        values_in_reversed_linked_list = []
        current_element = reversedLinkedList
        result = 0
        while True:
            values_in_reversed_linked_list.append(current_element.val)

            if current_element.next == None:
                break
            current_element = current_element.next
        
        for i in range(len(values_in_reversed_linked_list) -1, -1, -1):
            result = result + (values_in_reversed_linked_list[i] * pow(10, i))

        return result


    def buildRevesedLinkedListFromInt(self, value) -> ListNode:
        value_as_string = str(value)
        result = ListNode()
        current_node = result
        for i in range(len(value_as_string) -1, -1, -1):
            current_node.val = value_as_string[i]

            if(i == 0):
                break

            current_node.next = ListNode()
            current_node =  current_node.next

        return result

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_as_int = self.parseIntFromReversedLinkedList(l1)
        l2_as_int = self.parseIntFromReversedLinkedList(l2)
        result_as_int = l1_as_int + l2_as_int
        return self.buildRevesedLinkedListFromInt(result_as_int)


list_a = ListNode(9, ListNode(9, ListNode(9, ListNode(5))))
list_b = ListNode(5, ListNode(6, ListNode(7)))
solution = Solution()
print(solution.addTwoNumbers(list_a, list_b))