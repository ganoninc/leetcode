from typing import List
from collections import deque

class Solution:
    def getCellHash(self, i: int, j:int) -> str:
        return str(i) + "-" + str(j)

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = set()
        queue = deque()

        maze_length = len(maze)
        maze_height = len(maze[0])

        entrance_i, entrance_j = entrance
        queue.append((entrance_i, entrance_j, 0))

        visited.add(self.getCellHash(entrance[0], entrance[1]))

        directions = [(-1,0), (0,1), (1, 0), (0, -1)]

        while queue:
            i, j, move_count = queue.popleft()

            if move_count > 0 and (i == 0 or i == maze_length -1 or j == 0 or j == maze_height - 1):
                return move_count

            for i_offset, j_offset in directions:
                next_i = i + i_offset
                next_j = j + j_offset

                if next_i >= 0 and next_i < maze_length and next_j >= 0 and next_j < maze_height:

                    if maze[next_i][next_j] == "." and self.getCellHash(next_i, next_j) not in visited:
                        visited.add(self.getCellHash(next_i, next_j))
                        queue.append((next_i, next_j, move_count + 1))

        return -1
    
sol = Solution()
sol.nearestExit([["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], [1,2])