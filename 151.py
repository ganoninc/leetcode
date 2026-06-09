class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = []

        for c in s:
            if c != " ":
                word.append(c)
            elif len(word) > 0:
                words.append("".join(word))
                word = []

        if len(word) > 0:
            words.append("".join(word))

        return " ".join(reversed(words))
        

sol = Solution()
print(sol.reverseWords("  hello world  "))