# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        res = []
        
        node_to_be_visited_queue = deque([root])

        while node_to_be_visited_queue:
            node_of_level_count = len(node_to_be_visited_queue)

            for i in range(node_of_level_count):
                node = node_to_be_visited_queue.popleft()

                if i == node_of_level_count - 1:
                    res.append(node.val)

                if node.left:
                    node_to_be_visited_queue.append(node.left)

                if node.right:
                    node_to_be_visited_queue.append(node.right)

        return res