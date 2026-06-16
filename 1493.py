from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_count = 0
        max_length = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

                while zero_count > 1:
                    if nums[left] == 0:
                        zero_count -= 1

                    left += 1

            max_length = max(max_length, right - left) # the right formula is right - left + 1 for the actual length, and then - 1 for the 0 or 1 removed

        return max_length