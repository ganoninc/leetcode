# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def visiteNode(self, targetSum, subtotal, node, foundsPaths, currentPath):
        newCurrentPath = currentPath.copy()
        newCurrentPath.append(node.val)
        if node.left != None:
            self.visiteNode(targetSum, subtotal + node.val, node.left, foundsPaths, newCurrentPath)

        if node.right != None:
            self.visiteNode(targetSum, subtotal + node.val, node.right, foundsPaths, newCurrentPath)

        if node.left == None and node.right == None:
            if node.val + subtotal == targetSum:
                foundsPaths.append(newCurrentPath)
                


    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root == None:
            return []

        found_paths = []

        self.visiteNode(targetSum, 0, root, found_paths, [])
        return found_paths

solution = Solution()
print(solution.pathSum(TreeNode(1, TreeNode(3), TreeNode(2)), 4))