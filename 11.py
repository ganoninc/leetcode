from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_water_area = 0

        while i < j:
            min_height_index = i
            if height[j] < height[min_height_index]:
                min_height_index = j

            max_water_area = max(max_water_area, height[min_height_index] * (j- i))

            if min_height_index == i:
                i += 1
            else:
                j -= 1

        return max_water_area
    
solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
print(solution.maxArea([1,1]))