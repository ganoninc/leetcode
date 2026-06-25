from typing import List


class Solution:

    def resursiveBSToFindLowerEdgeOfTarget(self, nums, i, j, target, result):
        if i < 0:
            return

        if i >= j:
            if i >= 0 and nums[i-1] < target:
                result[0] = i
            return

        k = (j + i) // 2

        if nums[k] < target:
            self.resursiveBSToFindLowerEdgeOfTarget(nums, k + 1, j, target, result)
        elif nums[k] > target:
            self.resursiveBSToFindLowerEdgeOfTarget(nums, i,  k - 1, target, result)
        else:
            if k > 0:
                if nums[k-1] < target:
                    result[0] = k
                else:
                    self.resursiveBSToFindLowerEdgeOfTarget(nums, i, k-1, target, result)


    def resursiveBSToFindHigherEdgeOfTarget(self, nums, i, j, target, result):
        if j >= len(nums):
            return

        if i >= j:
            if i < len(nums) and nums[i+1] > target:
                result[1] = i
            return

        k = (j + i) // 2

        if nums[k] < target:
            self.resursiveBSToFindHigherEdgeOfTarget(nums, k + 1, j, target, result)
        elif nums[k] > target:
            self.resursiveBSToFindHigherEdgeOfTarget(nums, i,  k - 1, target, result)
        else:
            if k < len(nums):
                if nums[k+1] > target:
                    result[1] = k
                else:
                    self.resursiveBSToFindHigherEdgeOfTarget(nums, k +1, j, target, result)


    def recursiveBSToFindTarget(self, nums, i, j, target, result):
        if i >= j:
            return

        k = (j + i) // 2
        if nums[k] < target:
            self.recursiveBSToFindTarget(nums, k + 1, j, target, result)
        elif nums[k] > target:
            self.recursiveBSToFindTarget(nums, i, k - 1, target, result)
        else:
            result[0] = k;
            result[1] = k;
            self.resursiveBSToFindLowerEdgeOfTarget(nums, 0, k - 1, target, result)
            self.resursiveBSToFindHigherEdgeOfTarget(nums, k + 1,  len(nums), target, result)
        


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        if len(nums) == 0:
            return result

        if len(nums) == 1 and nums[0] == target:
            return [0,0]

        if len(nums) == 1 and nums[0] != target:
            return [-1,-1]
        
        self.recursiveBSToFindTarget(nums, 0, len(nums) - 1, target, result)

        return result


solution = Solution()
#print(solution.searchRange([5,7,7,8,8,10], 8))
# print(solution.searchRange([1], 0))
print(solution.searchRange([2,2], 2))