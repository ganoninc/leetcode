from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        result = 0
        maxHeightInRowIndex = []
        maxHeightInColumnIndex = []
        for i in range(0, len(grid)):
            maxHeightInRowIndex.append(-1)
            maxHeightInColumnIndex.append(-1)

        for rowIndex in range(0, len(grid)):
            for columnIndex in range(0, len(grid[rowIndex])):
                if maxHeightInRowIndex[rowIndex] == -1:
                    for i in range(0, len(grid[rowIndex])):
                        if grid[rowIndex][i] > maxHeightInRowIndex[rowIndex]:
                            maxHeightInRowIndex[rowIndex] = grid[rowIndex][i]

                if maxHeightInColumnIndex[columnIndex] == -1:
                    for i in range(0, len(grid)):
                        if grid[i][columnIndex] > maxHeightInColumnIndex[columnIndex]:
                            maxHeightInColumnIndex[columnIndex] = grid[i][columnIndex]

            
                result += min((maxHeightInRowIndex[rowIndex] - grid[rowIndex][columnIndex]), maxHeightInColumnIndex[columnIndex] - grid[rowIndex][columnIndex])

        return result

solution = Solution()
print(solution.maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))
print(solution.maxIncreaseKeepingSkyline([[0,0,0],[0,0,0],[0,0,0]]))