class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, node:TreeNode, max_ancestor: float) -> int:        
        left_branch_good_nodes = 0
        right_branch_good_nodes = 0

        if node.left:
            left_branch_good_nodes = self.dfs(node.left, max(max_ancestor, node.val))
        if node.right:
            right_branch_good_nodes = self.dfs(node.right, max(max_ancestor, node.val))

        return left_branch_good_nodes + right_branch_good_nodes + (1 if node.val >= max_ancestor else 0)

    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, float("-inf"))