# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def visitNode(self, node: Optional[TreeNode]) -> List[int]:
        if node == None:
            return []
        if node.left == None and node.right == None:
            return [node.val]
        else:
            return self.visitNode(node.left) + [node.val] + (self.visitNode(node.right))


    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.visitNode(root)


solution = Solution()
#print(solution.inorderTraversal(TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, TreeNode(3)))))
print(solution.inorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3), None))))