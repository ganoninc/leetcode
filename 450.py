# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        if root.val != key:
            if key < root.val:
                root.left = self.deleteNode(root.left, key)
            else:
                root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None or root.right is None:
                return root.left or root.right
            else:
                previous_in_order_node = root.left

                while previous_in_order_node.right:
                    previous_in_order_node = previous_in_order_node.right

                root.val = previous_in_order_node.val
                root.left = self.deleteNode(root.left, root.val)

        return root