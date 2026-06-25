from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        j = 0
        n = len(nums)

        while i < n and j < n:
            if nums[i] == 0:
                while j < n - 1 and nums[j] == 0:
                    j += 1
                
                if nums[j] != 0:
                    [nums[i], nums[j]] = [nums[j], nums[i]]
            elif i >= j:
                j = i + 1

            i += 1


sol = Solution()
print(sol.moveZeroes([1,0]))
print(sol.moveZeroes([0,1,0,3,12]))






