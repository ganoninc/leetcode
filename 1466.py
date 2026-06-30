from typing import List
from collections import defaultdict


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        min_reorder = 0
        visited_cities = set()
        stack = []
        city_connection_index = defaultdict(list)

        for i in range(len(connections)):
            city_connection_index[connections[i][0]].append(i)
            city_connection_index[connections[i][1]].append(i)

        visited_cities.add(0)
        stack.append(0)

        while stack:
            curr_city = stack.pop()
            visited_cities.add(curr_city)
            
            for connection_index in city_connection_index[curr_city]:
                origin, destination = connections[connection_index]

                needs_reorder = False

                if origin == curr_city:
                    next_city = destination
                    needs_reorder = True
                else:
                    next_city = origin

                if next_city in visited_cities:
                    continue
                    
                visited_cities.add(next_city)

                if needs_reorder:
                    min_reorder += 1

                stack.append(next_city)                        

        return min_reorder
    
sol = Solution()
sol.minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]])