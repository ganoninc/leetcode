from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0:1}
        subarray_count = 0
        acc = 0

        for num in nums:
            acc += num

            if acc - k in prefix_sums:
                subarray_count += prefix_sums[acc - k]


            if acc not in prefix_sums:
                prefix_sums[acc] = 0

            prefix_sums[acc] += 1

        return subarray_count
    

sol = Solution()
print(sol.subarraySum([1,2,1,2,1], 3))



# [1,1,1] k = 2
# acc = 1, acc - k = -1, not in prefix_sum {1 => 1}
# acc = 2, acc - k = 0, 0 not in prefix_sum


# 1 3 


# [1,1,1,3,2], 5
# acc 1   k-1 = 4    {1}
# acc 2   k-1 = 4    {1,2}
# acc 3   k-1 = 4    {1,2,3}
# acc 6   k-3 = 2     {1,2,3,6} <-- we have a 2 ! so one subarray
# acc 8   k-2 = 3     {1,2,3,6,8} <--- we have a 3 ! so two subarrays



# # Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# # A subarray is a contiguous non-empty sequence of elements within an array.



# # a subarray means sum of all values = K
# # we will need to check several times the sum of values of different subbaray --> prefixsum

# # [1,2,3,4,2,5] k = 5

# # [0, 1,3,6,10,12,17]

# # 0 1 = 1, 0 3 = 3, 0 6 = 6 > k
# # next
# # 1 3 = 2, 1 6 = 5 OK  -----------> { 1, 6}

# # 3 6 = 3, 3 10 = 7 > k
# # next
# # 6 10 = 4, 6 12 = 6 > k
# # next
# # 10 12 = 2, 10 17 = 7 > k
# # next
# # 12 17 = 5 OK ------->{ 1,6    12,17}





# # /////////////// HASHMAP


# # prefix = 0
# # for num in nums:
# #     prefix += num
# #     if(k-prefix in hashmap)
# #         count++

