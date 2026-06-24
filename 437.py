# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    res = 0

    def dfs(self, node: Optional[TreeNode], targetSum :int, prefix_sum_map: dict[int, int], ancestor_sum: int) -> None:
        if node is None:
            return
        
        current_sum = ancestor_sum + node.val
        if(current_sum - targetSum) in prefix_sum_map:
            self.res += (1 * prefix_sum_map[(current_sum - targetSum)])

        prefix_sum_map[current_sum] = prefix_sum_map.get(current_sum, 0) + 1

        self.dfs(node.left, targetSum, prefix_sum_map, current_sum)
        self.dfs(node.right, targetSum, prefix_sum_map, current_sum)

        prefix_sum_map[current_sum] = prefix_sum_map.get(current_sum, 0) - 1
            

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        
        self.dfs(root, targetSum, {0 : 1}, 0)

        return self.res
