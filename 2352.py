from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        equal_pairs_count = 0
        row_hashes_map = {}

        for row in grid:
            hash = ",".join(map(str, row))
            row_hashes_map[hash] = row_hashes_map.get(hash, 0) + 1

        for column_index in range(len(grid)):
            column_values = []
            for row_index in range(len(grid)):
                column_values.append(grid[row_index][column_index])

            hash = ",".join(map(str, column_values))
            if hash in row_hashes_map:
                equal_pairs_count += row_hashes_map[hash]

        return equal_pairs_count
    

sol = Solution()
print(sol.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))
        