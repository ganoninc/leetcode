
class Solution:
    def isPalindromic(self, s: str) -> bool:
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:

        s_length = len(s)

        if s_length == 1:
            return s

        longestPalindromicSubstring = ""
        for i in range(0, s_length):
            if len(longestPalindromicSubstring) > s_length - i:
                break

            if i + 1 < s_length:

                for j in range(s_length-1, i, -1):
                    if s[i] == s[j]:
                        if self.isPalindromic(s[i:j+1]):
                            if len(s[i:j+1]) > len(longestPalindromicSubstring):
                                longestPalindromicSubstring = s[i:j+1]


        if len(longestPalindromicSubstring) == 0:
            longestPalindromicSubstring = s[0]

        return longestPalindromicSubstring

solution = Solution()
print(solution.longestPalindrome("cbbd"))