
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> Optional[TreeNode]:
        if root.val == val:
            return root
        
        if val < root.val and root.left:
            return self.searchBST(root.left, val)
            
        if val > root.val and root.right:
            return self.searchBST(root.right, val)
        
        return None