from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        if len(nums) > 1:
            left = 0
            right = 1

            while right < len(nums):
                if nums[left] == 0:
                    if nums[right] == 0:
                        right += 1
                    else: 
                        nums[left] = nums[right]
                        nums[right] = 0

                        right += 1
                        left += 1
                else:
                    right += 1
                    left += 1

        # print(nums)

        

solution = Solution()
solution.moveZeroes([0,1,0,3,12])    
solution.moveZeroes([0,0,0,0])    
solution.moveZeroes([2,3,5,6])    
solution.moveZeroes([2,1]) 
solution.moveZeroes([]) 
solution.moveZeroes([1]) 