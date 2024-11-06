class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # A = 65, Z = 90
        result = []

        while columnNumber > 0:
            unit_value = (columnNumber - 1) % 26
            columnNumber = (columnNumber - 1) // 26

            result.append(chr(65 + unit_value))

        return ''.join(reversed(result))
    

solution = Solution()
print(solution.convertToTitle(1))
print(solution.convertToTitle(28))
print(solution.convertToTitle(701))