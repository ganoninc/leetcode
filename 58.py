class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word_length = 0
        i = len(s) - 1
        while s[i] == " ":
            i = i - 1

        while s[i] != " " and i >= 0:
            last_word_length = last_word_length + 1
            i = i - 1

        return last_word_length

        
solution = Solution()
k = solution.lengthOfLastWord("   fly me   to   the moon  ")
print(k)