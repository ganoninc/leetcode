# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import List, Optional


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if root is None:
            return res
        
        queue = [root]
        queue_index = 0

        while queue_index < len(queue):
            nodes_of_current_level = []
            current_level_queue_size = len(queue)

            for i in range(queue_index, current_level_queue_size):
                node = queue[i]
                queue_index += 1
                nodes_of_current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(nodes_of_current_level)

        return res
