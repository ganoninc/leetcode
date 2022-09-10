# Definition for a binary tree node.
import string
from typing import List, Optional
from unicodedata import digit


class TreeNode:
    def __init__(self, val=""):
        self.val = val
        self.sons = []


class Solution:
    alphabet = {
        "2": ['a', 'b', 'c'],
        "3": ['d','e','f'],
        "4": ['g','h','i'],
        "5": ['j','k','l'],
        "6": ['m','n','o'],
        "7": ['p','q','r', 's'],
        "8": ['t', 'u', 'v'],
        "9": ['w', 'x', 'y', 'z'],
    }

    def addTreeNodesToTreeEnds(self, tree_node_values: List, tree: TreeNode):
        if len(tree.sons) == 0:
            for tree_node_value in tree_node_values:
                tree.sons.append(TreeNode(tree_node_value))

        else:
            for son in tree.sons:
                self.addTreeNodesToTreeEnds(tree_node_values, son)



    def buildSolutionsTree(self, digits: str) -> TreeNode:
        tree = TreeNode()
        for i in range(0, len(digits)):
            self.addTreeNodesToTreeEnds(self.alphabet[digits[i]], tree)
        return tree


    def findAllSolutionsInTree(self, tree: TreeNode, all_solutions: List, tmp_solution : string) -> None:
        if len(tree.sons) == 0:
            all_solutions.append(tmp_solution)
        else:
            for son in tree.sons:
                self.findAllSolutionsInTree(son, all_solutions, tmp_solution + son.val)


    
    def getAllSolutionsFromSolutionsTree(self, tree: TreeNode) -> List:
        all_solutions = []
        self.findAllSolutionsInTree(tree, all_solutions, "")
        return all_solutions



    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if digits == "":
            return result

        solutions_tree = self.buildSolutionsTree(digits)
        result = self.getAllSolutionsFromSolutionsTree(solutions_tree)
        # print(solutions_tree)
        return result


solution = Solution()
print(solution.letterCombinations("23"))