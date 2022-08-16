from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        isSimilarResultSet = self.isSimilar(head, [])
        return isSimilarResultSet["result"]

    def isSimilar(self, element: ListNode, encountedElementsAsArray): 
        encountedElementsAsArray.append(element.val)
        if element.next == None:
            if element.val == encountedElementsAsArray[0]:
                return {"result":True, "index_to_be_checked": 1, "listLength": len(encountedElementsAsArray)}
            else:
                return {"result":False, "index_to_be_checked": 1, "listLength": len(encountedElementsAsArray)}
        else:
            isSimilarResultSet = self.isSimilar(element.next, encountedElementsAsArray)
            if isSimilarResultSet["result"] == True:
                shall_continue = False
                if isSimilarResultSet["listLength"] % 2 == 0 and isSimilarResultSet["index_to_be_checked"] <= isSimilarResultSet["listLength"] / 2:
                    shall_continue = True
                elif isSimilarResultSet["listLength"] % 2 != 0 and isSimilarResultSet["index_to_be_checked"] < isSimilarResultSet["listLength"] // 2 + 1:
                    shall_continue = True

                if shall_continue == True:
                    if element.val == encountedElementsAsArray[isSimilarResultSet["index_to_be_checked"]]:
                        return {"result":True, "index_to_be_checked": isSimilarResultSet["index_to_be_checked"] + 1, "listLength": isSimilarResultSet["listLength"]}
                    else:
                        return {"result":False, "index_to_be_checked": isSimilarResultSet["index_to_be_checked"] + 1, "listLength": isSimilarResultSet["listLength"]}
                else:
                    return isSimilarResultSet
            else:
                return {"result":False, "index_to_be_checked": isSimilarResultSet["index_to_be_checked"] + 1, "listLength": isSimilarResultSet["listLength"]}

solution = Solution()
list_a = ListNode(1, ListNode(2, ListNode(1)))
print(solution.isPalindrome(list_a))