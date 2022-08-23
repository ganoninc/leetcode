class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        substring_index = -1
        for i in range(0,len(haystack)):
            if substring_index != -1:
                break
            if haystack[i] == needle[0]:
                if haystack[i:i+len(needle)] == needle:
                    substring_index = i

        return substring_index

solution = Solution()
print(solution.strStr("hello", "ll"))
print(solution.strStr("aaaaa", "bba"))