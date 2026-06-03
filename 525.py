from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        earliest_balances = {}
        balance = 0
        earliest_balances[0] = 0
        max_length = 0

        for i in range(0, len(nums)):
            if(nums[i] == 0):
                balance -= 1
            else:
                balance += 1

            if balance in earliest_balances:
                max_length = max(max_length, (i + 1 - earliest_balances[balance]))
            else:
                earliest_balances[balance] = i + 1

        return max_length
    

solution = Solution()
print(solution.findMaxLength([0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1]))

