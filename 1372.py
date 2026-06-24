# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

LEFT_DIRECTION = -1
NO_DIRECTION = 0
RIGHT_DIRECTION = +1
        
class Solution:
    res = 0

    def dfs(self, node : Optional[TreeNode], ancestor_sum: int, origin: int) ->None:
        if node is None:
            return
        
        curr_sum = ancestor_sum + 1
        self.res = max(self.res, curr_sum)

        self.dfs(node.left, 1 if origin == LEFT_DIRECTION else curr_sum, LEFT_DIRECTION)
        self.dfs(node.right, 1 if origin == RIGHT_DIRECTION else curr_sum, RIGHT_DIRECTION)


    def longestZigZag(self, root: TreeNode) -> int:
        self.dfs(root, 0, NO_DIRECTION)
        return self.res -1;