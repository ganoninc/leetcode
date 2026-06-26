# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        max_sum = float("-inf")
        max_sum_index = 0
        level_index = 1
        queue = [root]
        queue_start_index = 0

        while queue_start_index < len(queue):
            level_size = len(queue)
            level_sum = 0

            for i in range(queue_start_index, level_size):
                node = queue[i]
                queue_start_index += 1

                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_sum_index = level_index

            level_index += 1

        return max_sum_index


        