class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == "]":
                substring = ""
                while stack[-1] != "[":
                    substring_c = stack.pop()
                    substring = substring_c + substring

                stack.pop() # pops the matching '[' out of the stack

                multiplier = 1
                nb_of_times = 0
                while len(stack) > 0 and stack[-1].isnumeric():
                    digit_from_stack = stack.pop()
                    nb_of_times += int(digit_from_stack) * multiplier
                    multiplier *= 10
                
                stack.append(nb_of_times * substring)

            else:
                stack.append(c)

        return "".join(stack)
    
sol = Solution()
print(sol.decodeString("3[a]2[bc]"))