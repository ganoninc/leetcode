# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left_branch_depth = self.maxDepth(root.left)
        right_branch_depth = self.maxDepth(root.right)

        return max(left_branch_depth, right_branch_depth) + 1