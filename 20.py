class Solution:
    def isValid(self, s: str) -> bool:
        is_valid = True
        expected_closing_parentheses = []
        for parenthese in s:

            if is_valid == False:
                break

            if parenthese == "(":
                expected_closing_parentheses.append(")")
            elif parenthese == "[":
                expected_closing_parentheses.append("]")
            elif parenthese == "{" :
                expected_closing_parentheses.append("}")
            
            elif parenthese == ")":
                if len(expected_closing_parentheses) == 0:
                    is_valid = False
                else:
                    if parenthese != expected_closing_parentheses.pop():
                        is_valid = False
            elif parenthese == "]":
                if len(expected_closing_parentheses) == 0:
                    is_valid = False
                else:
                    if parenthese != expected_closing_parentheses.pop():
                        is_valid = False
            elif parenthese == "}":
                if len(expected_closing_parentheses) == 0:
                    is_valid = False
                else:
                    if parenthese != expected_closing_parentheses.pop():
                        is_valid = False

        if len(expected_closing_parentheses) > 0:
            is_valid = False

        return is_valid
        
solution = Solution()
print(solution.isValid("]"))