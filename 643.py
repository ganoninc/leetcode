from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_average_value = 0
        window_sum = 0
        
        for l in range(0, k):
            window_sum += nums[l]
        max_average_value = window_sum / k

        i = 1
        j = i + k - 1

        while j < len(nums):
            window_sum -= nums[i-1]
            window_sum += nums[j]
            max_average_value = max(max_average_value, window_sum / k)
            i += 1
            j += 1

        return max_average_value

sol = Solution()
print(sol.findMaxAverage([1,12,-5,-6,50,3], 4))

# [1,12,-5,-6,50,3] k =4
# window_sum = 2 / average 0.5
# window_sum = 51 / average 12,75
# window_sum = 42 / average 10,5