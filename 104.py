# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def visiteNode(self, node, deepIndex, deepIndexes):
        if node.left != None:
            self.visiteNode(node.left, deepIndex +1, deepIndexes)

        if node.right != None:
            self.visiteNode(node.right, deepIndex + 1, deepIndexes)

        if node.left == None and node.right == None:
            deepIndexes.append(deepIndex)


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        if root.left == None and root.right == None:
            return 1

        deepIndexes = []
        self.visiteNode(root, 0,deepIndexes)
        found_max = -1
        found_min = 100000

        for i in range(0, len(deepIndexes)):
            if deepIndexes[i] > found_max:
                found_max = deepIndexes[i]

            if deepIndexes[i] < found_min:
                found_min = deepIndexes[i]
            
        return found_max + 1


b = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
solution = Solution()
print(solution.maxDepth(b))