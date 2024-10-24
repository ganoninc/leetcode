# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        postorder_traversal = self.postorderTraversal(root.left)
        postorder_traversal.extend(self.postorderTraversal(root.right))
        postorder_traversal.extend([root.val])
            
        return postorder_traversal


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    index = 1

    while queue and index < len(values):
        current = queue.pop(0)

        # Add left child
        if values[index] is not None:
            current.left = TreeNode(values[index])
            queue.append(current.left)
        index += 1

        # Add right child
        if index < len(values) and values[index] is not None:
            current.right = TreeNode(values[index])
            queue.append(current.right)
        index += 1

    return root
        

solution = Solution()
# root1 = TreeNode(1)
# root1.left = TreeNode(2)
# root1.right = TreeNode(3)
# root1.left.left = TreeNode(4)
# root1.left.right = TreeNode(5)
# print(solution.postorderTraversal(root1))

values = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]
root2 = build_tree(values)
print(solution.postorderTraversal(root2))