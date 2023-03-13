# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return root

        largestValues = []

        q = []
        q.append(root)
        level = 0

        while len(q) > 0:
            level_node_count = len(q)
            while level_node_count > 0:
                node = q.pop(0)

                if len(largestValues) < (level + 1):
                    largestValues.append(node.val)
                elif largestValues[level] < node.val:
                    largestValues[level] = node.val

                if node.left != None:
                    q.append(node.left)

                if node.right != None:
                    q.append(node.right)

                level_node_count = level_node_count - 1
            level +=1

        return largestValues


solution = Solution()
# print(solution.largestValues(TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))))
# print(solution.largestValues(TreeNode(1, None, TreeNode(2))))
print(solution.largestValues(TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))))