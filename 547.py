from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        stack = []
        visited_nodes = set()
        province_count = 0
        number_of_nodes = len(isConnected)
            
        for i in range(number_of_nodes):
            if i in visited_nodes:
                continue

            stack.append(i)
            visited_nodes.add(i)
            province_count += 1

            while stack:
                curr_node = stack.pop()

                for j in range(number_of_nodes):
                    if isConnected[curr_node][j] and j not in visited_nodes:
                        visited_nodes.add(j)
                        stack.append(j)

            
        return province_count
    
sol = Solution()
sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]])
sol.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])