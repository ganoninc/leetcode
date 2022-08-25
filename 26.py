from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_read_value = -101
        i = 0
        unique_value_index = 0
        while(i < len(nums)):
            if nums[i] > last_read_value:
                nums[unique_value_index] = nums[i]
                last_read_value = nums[i]
                unique_value_index = unique_value_index + 1

            i = i + 1

        return unique_value_index


solution = Solution()
input_array = [1,1,2]
k = solution.removeDuplicates(input_array)
print(k)
print(input_array)