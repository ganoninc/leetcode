# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def dfs(self, node: Optional[TreeNode], targetSum: int, ancestor_sum) -> bool:
        if node is None:
            return False
        
        current_sum = ancestor_sum + node.val

        if current_sum == targetSum and node.left is None and node.right is None:
            return True
        
        return self.dfs(node.left, targetSum, ancestor_sum=current_sum) or self.dfs(node.right, targetSum, ancestor_sum=current_sum)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.dfs(root, targetSum, 0)
        