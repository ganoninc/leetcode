# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: ListNode) -> int:
        slow = head
        fast = head
        res = 0

        while fast and fast.next:
            fast = fast.next.next
            assert slow is not None
            slow = slow.next

        assert slow is not None
        curr = slow
        prev = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        list1_curr = head
        list2_curr = prev

        while list1_curr and list2_curr:
            res = max(res, list1_curr.val + list2_curr.val)
            list1_curr = list1_curr.next
            list2_curr = list2_curr.next

        return res