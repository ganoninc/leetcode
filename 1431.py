from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_qtt = max(candies)
        res = []

        for qtt in candies:
            res.append(qtt + extraCandies >= max_qtt)

        return res
    
sol = Solution()
print(sol.kidsWithCandies([2,3,5,1,3], 3))