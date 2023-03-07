from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def visiteNode(self, q, nodesPerDeepIndex):
        decoratedNode = q.pop(0)
        if decoratedNode["node"] is not None:
            nodesPerDeepIndex[decoratedNode["deepIndex"]].append(decoratedNode["node"])
            q.append({
                "node":decoratedNode["node"].left,
                "deepIndex": decoratedNode["deepIndex"]+1
            })
            q.append({
                "node":decoratedNode["node"].right,
                "deepIndex": decoratedNode["deepIndex"]+1
            })
            self.visiteNode(q, nodesPerDeepIndex)


    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return

        nodesPerDeepIndex = [[] for i in range(64)]
        q = []
        q.append({
            "node":root,
            "deepIndex": 0
        })

        self.visiteNode(q, nodesPerDeepIndex)
        # print(nodesPerDeepIndex)

        for i in range(0, len(nodesPerDeepIndex)):
            for j in range(0, len(nodesPerDeepIndex[i])):
                if j < len(nodesPerDeepIndex[i]) - 1:
                    nodesPerDeepIndex[i][j].next = nodesPerDeepIndex[i][j+1]
                    
        return root


solution = Solution()
aTree = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
print(solution.connect(aTree))