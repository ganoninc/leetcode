import re

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd = ""

        if len(str1) > len(str2):
            temp = str1
            str1 = str2
            str2 = temp
        
        for i in range(1, len(str1) + 1):
            candidate_subtr = str1[0:i]
            re_filter = r"(" + candidate_subtr + ")*"
            remainder_of_str1 = re.sub(re_filter, "", str1)
            remainder_of_str2 = re.sub(re_filter, "", str2)

            if len(remainder_of_str1) == 0 and len(remainder_of_str2) == 0:
                gcd = candidate_subtr

        return gcd


sol = Solution()
print(sol.gcdOfStrings("ABCABC", "ABC"))