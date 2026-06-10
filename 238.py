from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix_product = 1
        sufix_product = 1
        prefix_products = [1] * (len(nums) + 1)
        sufix_products = [1] * (len(nums) + 1)

        i = 0
        j = len(nums) - 1

        while i < len(nums) and j >= 0 :
            prefix_product = prefix_product * nums[i]
            prefix_products[i+1] = prefix_product
            i = i + 1

            sufix_product = sufix_product * nums[j]
            sufix_products[j] = sufix_product
            j = j - 1

        for i in range(0, len(nums)):
            res.append(prefix_products[i] * sufix_products[i+1])

        return res


sol = Solution()
print(sol.productExceptSelf([3,5,2,5]))

#   [3,5,2,5]
# [1,1, 3,15, 30]   
# [1,3,15,30,150]

