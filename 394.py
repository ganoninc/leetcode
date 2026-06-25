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
    
# sol = Solution()
# print(sol.decodeString("32[a]2[bc]"))


def stacky(s):
    """
    When we hit an open bracket, we know we have parsed k for the contents of the bracket, so 
    push (current_string, k) to the stack, so we can pop them on closing bracket to duplicate
    the enclosed string k times.
    """
    stack = []
    current_string = ""
    k = 0
    
    for char in s:
        if char == "[":
            # Just finished parsing this k, save current string and k for when we pop
            stack.append((current_string, k))
            # Reset current_string and k for this new frame
            current_string = ""
            k = 0
        elif char == "]":
            # We have completed this frame, get the last current_string and k from when the frame 
            # opened, which is the k we need to duplicate the current current_string by
            last_string, last_k = stack.pop(-1)
            current_string = last_string + last_k * current_string
        elif char.isdigit():
            k = k * 10 + int(char)
        else:
            current_string += char
    
    return current_string

print(stacky("32[az]fg2[bc]"))