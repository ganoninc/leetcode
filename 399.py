from typing import List, Optional
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        res = []
        adjacency_list = defaultdict(list)

        for i in range(len(equations)):
            a, b = equations[i]
            weight = values[i]
            adjacency_list[a].append((b, weight))
            adjacency_list[b].append((a, 1 / weight))

        def dfs(node: str , target: str, acc: float, visited: set[str]) -> float:
            if node not in adjacency_list or target not in adjacency_list:
                return -1 
            
            if node == target:
                return acc
            
            visited.add(node)
            
            for adjancent_node in adjacency_list[node]:
                neighbor, weight = adjancent_node
                if neighbor not in visited:
                    result = dfs(neighbor, target, acc * weight, visited)
                    if result != -1:
                        return result
                
            return -1


        for query in queries:
            start = query[0]
            end = query[1]
            visited = set()

            res.append(dfs(start, end, 1, visited))

        return res


sol = Solution()
sol.calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])

