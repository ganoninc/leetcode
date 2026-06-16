from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        flip_count = 0
        longuest_length = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                flip_count += 1

            while flip_count > k :
                if nums[left] == 0:
                    flip_count -= 1
                left += 1

            longuest_length = max(longuest_length, right - left + 1)

        return longuest_length


sol = Solution()
sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)
sol.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)
