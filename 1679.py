from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums_count = {}
        max_operations = 0

        for num in nums:
            target = k - num

            if target in nums_count and nums_count[target] > 0:
                max_operations += 1
                nums_count[target] = nums_count[target] - 1
            else:
                if num not in nums_count:
                    nums_count[num] = 0

                nums_count[num] = nums_count[num] + 1

        return max_operations
