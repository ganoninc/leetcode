class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        power_index = 0

        for i in reversed(columnTitle):
            letter_value = ord(i) - 64 # A = 65, but this is 1 indexed, so A - 1
            letter_value = letter_value * pow(26, power_index)
            power_index = power_index + 1
            result = result + letter_value

        return result

solution = Solution()
print(solution.titleToNumber("AB"))
print(solution.titleToNumber("ZY"))