# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def recursiveBFS(self, q, discoveredNodes):
        if not q :
            return
        
        n = q.popleft()

        if n["node"].left == None:
            child_node = {
                'node':TreeNode(-101),
                'deepLevel': n["deepLevel"] + 1
            }
            discoveredNodes.append(child_node)

        if n["node"].left != None and n["node"].left not in discoveredNodes:
            child_node = {
                'node':n["node"].left,
                'deepLevel': n["deepLevel"] + 1
            }
            discoveredNodes.append(child_node)
            q.append(child_node)

        if n["node"].right == None:
            child_node = {
                'node':TreeNode(-101),
                'deepLevel': n["deepLevel"] + 1
            }
            discoveredNodes.append(child_node)

        if n["node"].right != None and n["node"].right not in discoveredNodes:
            child_node = {
                'node':n["node"].right,
                'deepLevel': n["deepLevel"] + 1
            }
            discoveredNodes.append(child_node)
            q.append(child_node)
        
        self.recursiveBFS(q, discoveredNodes)


    def isEveryLevelAPalindrome(self, discoveredNodes) -> bool:
        currentReviewdDeepIndex = 1
        nodesInCurrentlyReviwedIndex = []
        for i in range(1, len(discoveredNodes)): #let's skip the first level, because it's always a single node
            if discoveredNodes[i]["deepLevel"] != currentReviewdDeepIndex:
                if len(nodesInCurrentlyReviwedIndex) % 2 != 0:
                    return False
                for j in range(0, len(nodesInCurrentlyReviwedIndex)):
                    if j < len(nodesInCurrentlyReviwedIndex) / 2:
                        if nodesInCurrentlyReviwedIndex[j] != nodesInCurrentlyReviwedIndex[len(nodesInCurrentlyReviwedIndex) - j -1]:
                            return False

                nodesInCurrentlyReviwedIndex = []
                currentReviewdDeepIndex = currentReviewdDeepIndex +1
                nodesInCurrentlyReviwedIndex.append(discoveredNodes[i]["node"].val)

            else:
                nodesInCurrentlyReviwedIndex.append(discoveredNodes[i]["node"].val)

        if len(nodesInCurrentlyReviwedIndex) % 2 != 0:
            return False
        for j in range(0, len(nodesInCurrentlyReviwedIndex)):
            if j < len(nodesInCurrentlyReviwedIndex) / 2:
                if nodesInCurrentlyReviwedIndex[j] != nodesInCurrentlyReviwedIndex[len(nodesInCurrentlyReviwedIndex) - j -1]:
                    return False

        return True


    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return False

        q = deque()
        discoveredNodes = [] #The number of nodes in the tree is in the range [1, 1000].
        start_node = {
            'node':root,
            'deepLevel': 0
        }
        discoveredNodes.append(start_node)
        q.append(start_node)
        self.recursiveBFS(q, discoveredNodes)
        return self.isEveryLevelAPalindrome(discoveredNodes)

solution = Solution()
# print(solution.isSymmetric(TreeNode(1, TreeNode(2, TreeNode(5), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(5)))))
# print(solution.isSymmetric(TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))))
print(solution.isSymmetric(TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, TreeNode(3)))))