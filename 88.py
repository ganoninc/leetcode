from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1_index = m - 1
        nums2_index = n - 1

        rewrite_index = m + n - 1

        while nums1_index >= 0 and nums2_index >= 0:
            if nums1[nums1_index] < nums2[nums2_index]:
                nums1[rewrite_index] = nums2[nums2_index]
                rewrite_index = rewrite_index - 1
                nums2_index = nums2_index - 1
            elif nums1[nums1_index] > nums2[nums2_index]:
                nums1[rewrite_index] = nums1[nums1_index]
                rewrite_index = rewrite_index - 1
                nums1_index = nums1_index - 1
            else:
                nums1[rewrite_index] = nums1[nums1_index]
                nums1_index = nums1_index - 1
                rewrite_index = rewrite_index - 1

        while nums2_index >= 0:
            nums1[rewrite_index] = nums2[nums2_index]
            rewrite_index = rewrite_index - 1
            nums2_index = nums2_index - 1

solution = Solution()

# list1 = [4,0,0,0,0,0]
# list2 = [1,2,3,5,6]

# solution.merge(list1, 1, list2, 5)
# print(list1)

list1 = [1,2,3,0,0,0]
list2 = [2,5,6]

solution.merge(list1, 3, list2, 3)
print(list1)