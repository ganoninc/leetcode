# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def visiteNode(self, targetSum, subtotal, node):
        is_left_valid = False
        is_right_valid = False
        if node.left != None:
            is_left_valid = self.visiteNode(targetSum, subtotal + node.val, node.left)

        if node.right != None:
            is_right_valid = self.visiteNode(targetSum, subtotal + node.val, node.right)

        if is_left_valid or is_right_valid:
            return True

        if node.left == None and node.right == None:
            if node.val + subtotal == targetSum:
                return True
                
                
        return False



    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False

        return self.visiteNode(targetSum, 0, root)

solution = Solution()
# print(solution.hasPathSum(TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, TreeNode(3))), 4))
print(solution.hasPathSum(TreeNode(1, TreeNode(2), TreeNode(3)), 4))