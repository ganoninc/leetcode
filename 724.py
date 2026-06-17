from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sums = [0]
        sum = 0

        for num in nums:
            sum += num
            prefix_sums.append(sum)

        for i in range(len(nums)):
            if prefix_sums[i] - prefix_sums[0] == prefix_sums[-1] - prefix_sums[i+1]:
                return i

        return -1
    

sol = Solution()
sol.pivotIndex([1,7,3,6,5,6])