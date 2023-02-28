from typing import List


class Solution:
    # function found on https://stackoverflow.com/questions/2267362/how-to-convert-an-integer-to-a-string-in-any-base
    def numberToBase(self, n, b):
        if n == 0:
            return [0]
        digits = []
        while n:
            digits.append(int(n % b))
            n //= b
        return digits[::-1]


    def isPalindromic(self, digits: List) -> bool:
        if len(digits) % 2 != 0:
            return False
        else:
            isPalindromicResult = True
            j = len(digits) - 1
            i = 0
            while i < j:
                if digits[i] != digits[j]:
                    isPalindromicResult = False

                i += 1
                j -= 1

            return isPalindromicResult



    def isStrictlyPalindromic(self, n: int) -> bool:
        return self.isStrictlyPalindromicRecursive(n, n-2)


    def isStrictlyPalindromicRecursive(self, n: int, base: int) -> bool:
        if base < 2:
            return True
        else:
            if self.isStrictlyPalindromicRecursive(n, base - 1):
                return self.isPalindromic(self.numberToBase(n, base))
            else: 
                return False


solution = Solution()
# solution.isPalindromic([2, 3, 5, 6, 3, 2])
print(solution.isStrictlyPalindromic(9))