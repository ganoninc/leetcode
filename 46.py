from typing import List


class Solution:
    def dfs(self, tmpSolution, remainingNumbers, foundSolutions):
        if len(remainingNumbers) == 0:
            foundSolutions.append(tmpSolution)
        else:
            for remainingNumber in remainingNumbers:
                self.dfs(tmpSolution  + [remainingNumber], [x for x in remainingNumbers if x != remainingNumber], foundSolutions)

    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return nums
        solutions = []
        self.dfs([], nums, solutions)
        return solutions


solution = Solution()
print(solution.permute([1,2,3]))