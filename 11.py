from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area_result = 0
        i = 0
        j = len(height) - 1

        while j != i:
            lowest_vertical_line_index = -1
            if height[i] > height[j]:
                lowest_vertical_line = height[j]
                lowest_vertical_line_index = j
            elif height[i] < height[j]:
                lowest_vertical_line = height[i]
                lowest_vertical_line_index = i
            else:
                lowest_vertical_line = height[i]
                lowest_vertical_line_index = i

            amount_of_water = lowest_vertical_line * (j - i)

            if max_area_result < amount_of_water:
                max_area_result = amount_of_water

            if lowest_vertical_line_index == i:
                i = i + 1
            else:
                j = j - 1

        return max_area_result
    
solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
print(solution.maxArea([1,1]))