# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def visite(self, p_node, q_node, visited_p_node, visited_q_node) -> bool:
        if p_node == None and q_node != None:
            return False

        if p_node != None and q_node == None:
            return False

        if p_node == None and q_node == None:
            return True

        if p_node.val != q_node.val:
            return False
        
        if p_node not in visited_p_node and q_node not in visited_q_node:
            visited_p_node.append(p_node)
            visited_q_node.append(q_node)
            if p_node.left != None:
                if not self.visite(p_node.left, q_node.left, visited_p_node, visited_q_node):
                    return False
                
            if p_node.right != None:
                if not self.visite(p_node.right, q_node.right, visited_p_node, visited_q_node):
                    return False

            if p_node.left == None and q_node.left != None:
                return False

            if p_node.right == None and q_node.right != None:
                return False

            return True

        elif p_node not in visited_p_node and q_node in visited_q_node:
            return False
            
        elif p_node in visited_p_node and q_node not in visited_q_node:
            return False

        else:
            return True


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        visited_p_node = []
        visited_q_node = []
        return self.visite(p, q, visited_p_node, visited_q_node)

        

# a = TreeNode(1,TreeNode(2),TreeNode(3, TreeNode(2)))
# b = TreeNode(1,TreeNode(2),TreeNode(3))

a = TreeNode(1)
b = TreeNode(1,None,TreeNode(3))
solution = Solution()
print(solution.isSameTree(a, b))