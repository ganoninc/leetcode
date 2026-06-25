# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, node: Optional[TreeNode], p, q,)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root is None:
            return
        
        if root == p:
            return root
        
        if root == q:
            return root
        
        q_in_branch = None
        p_in_branch = None
        if root.left:
            q_in_branch = self.lowestCommonAncestor(root.left, p, q)
            p_in_branch = self.lowestCommonAncestor(root.left, p, q)