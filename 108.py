# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        
        i = len(nums) // 2
        
        return TreeNode(nums[i], self.sortedArrayToBST(nums[0:i]), self.sortedArrayToBST(nums[i+1:]))
    

solution = Solution()
print(solution.sortedArrayToBST([-10,-3,0,5,9]))