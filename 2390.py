class Solution:
    def removeStars(self, s: str) -> str:
        ans_stack = []
        for c in s:
            if c == '*':
                ans_stack.pop()
            else:
                ans_stack.append(c)

        return "".join(ans_stack)
