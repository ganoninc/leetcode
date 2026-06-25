# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    lowest_common_ancestor = TreeNode(0)

    def dfs(self, node: Optional[TreeNode], p: TreeNode, q: TreeNode) -> int:
        if node is None:
            return 0
        
        found_count = 0
        if node.val == p.val or node.val == q.val:
            found_count += 1

        found_count += self.dfs(node.left, p, q) + self.dfs(node.right, p, q)

        if found_count == 2:
            self.lowest_common_ancestor = node
            found_count = 0

        return found_count

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lowest_common_ancestor = TreeNode(0)
        self.dfs(root, p, q)
        return self.lowest_common_ancestor