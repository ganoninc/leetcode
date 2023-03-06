# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def recursiveDFS(self, node, visitedNodes):
        if node != None:
            visitedNodes.append(node)

            if node.left != None:
                self.recursiveDFS(node.left, visitedNodes)

            if node.right != None:
                self.recursiveDFS(node.right, visitedNodes)



    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        visitedNodes = []
        self.recursiveDFS(root, visitedNodes)
        for i in range(0, len(visitedNodes) - 1):
            visitedNodes[i].left = None
            visitedNodes[i].right = visitedNodes[i+1]


solution = Solution()
tree = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
solution.flatten(tree)
print(tree)