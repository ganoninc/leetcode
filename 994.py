from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        orange_count = 0
        rotten_orange_count = 0
        minute_count = 0
        queue = deque()
        grid_height = len(grid)
        grid_width = len(grid[0])

        for i in range(grid_height):
            for j in range(grid_width):
                if grid[i][j] != 0:
                    orange_count += 1
                    
                    if grid[i][j] == 2:
                        rotten_orange_count += 1
                        queue.append((i,j))

        directions = [(-1,0), (0,1), (1,0), (0,-1)]

        while queue:
            rotted_this_minute = False
            queue_size = len(queue)

            for k in range(queue_size):
                i,j = queue.popleft()

                for i_offset, j_offset in directions:
                    next_i = i + i_offset
                    next_j = j + j_offset

                    if next_i < 0 or next_i >= grid_height or next_j < 0 or next_j >= grid_width:
                        continue

                    if grid[next_i][next_j] == 1:
                        grid[next_i][next_j] = 2
                        rotten_orange_count += 1
                        rotted_this_minute = True
                        queue.append((next_i, next_j))

            if rotted_this_minute:
                minute_count += 1

        if rotten_orange_count == orange_count:
            return minute_count
        else:
            return -1