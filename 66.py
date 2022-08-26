from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_value = 0
        pow_index = 0
        for i in range(len(digits) -1, -1, -1):
            digits_value = digits_value + digits[i] * pow(10, pow_index)
            pow_index = pow_index + 1

        digits_value = digits_value + 1

        return list(str(digits_value))
        

solution = Solution()
print(solution.plusOne([1,3,9]))