# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def get_leaf_sequence(self, node: TreeNode, leaf_sequence: list[int]) -> None:
        if node.left is None and node.right is None:
            leaf_sequence.append(node.val)
            return
        
        if node.left:
            self.get_leaf_sequence(node.left, leaf_sequence)
        
        if node.right:
            self.get_leaf_sequence(node.right, leaf_sequence)
            

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaf_sequence_1 = []
        leaf_sequence_2 = []

        self.get_leaf_sequence(root1, leaf_sequence_1)
        self.get_leaf_sequence(root2, leaf_sequence_2)

        return leaf_sequence_1 == leaf_sequence_2