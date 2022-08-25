from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        cleaned_value_index = 0
        while(i < len(nums)):
            if nums[i] != val:
                nums[cleaned_value_index] = nums[i]
                cleaned_value_index = cleaned_value_index + 1
            i = i + 1

        return cleaned_value_index


solution = Solution()
input_array = [3,2,2,3]
k = solution.removeElement(input_array, 3)
print(k)
print(input_array)