class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        res = list(s)

        while left < right:
            if self.isVowel(s[left]) and self.isVowel(s[right]):
                [res[left], res[right]] = [res[right], res[left]]
                left += 1
                right -= 1
            elif self.isVowel(s[left]):
                right -= 1
            elif self.isVowel(s[right]):
                left += 1
            else:
                left += 1
                right -= 1

        return "".join(res)
    
    def isVowel(self, c: str) -> bool:
        lowered_c = c.lower()
        return lowered_c == "a" or lowered_c == "e" or lowered_c == "i" or lowered_c == "o" or lowered_c == "u"
    
sol = Solution()
print(sol.reverseVowels("IceCreAm"))