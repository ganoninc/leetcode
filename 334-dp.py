from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        LIS = [1] * len(nums)

        for i in range(len(nums) -2, -1, -1):
            candidates = []
            for j in range(i + 1, len(nums)):
                if(nums[i] < nums[j]):
                    candidates.append(1 + LIS[j])

            LIS[i] = max([1] + candidates)
            if LIS[i] > 2:
                return True

        return False

    
sol = Solution()
print(sol.increasingTriplet([1,5,0,7]))