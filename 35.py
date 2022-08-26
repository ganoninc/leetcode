from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(0, len(nums)):
            if nums[i] == target:
                return i
            else:
                if nums[i] > target:
                    return i

        return len(nums)
        

solution = Solution()
input_array = [1,3,5,6]
k = solution.searchInsert(input_array, 7)
print(k)