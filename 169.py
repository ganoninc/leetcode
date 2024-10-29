from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element_count = {}
        target = len(nums) / 2

        if target == 0.5:
            return nums[0]

        for num in nums:
            if num in element_count:
                element_count[num] = element_count[num] + 1
                if element_count[num] > target:
                    return num
            else:
                element_count[num] = 1


solution = Solution()
print(solution.majorityElement([2,2,1,1,1,2,2]))
print(solution.majorityElement([2]))