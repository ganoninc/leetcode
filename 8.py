import string


class Solution:
    SYMBOL_WHITE_SPACE = "SYMBOL_WHITE_SPACE"
    SYMBOL_NEGATIVE_SIGN = "SYMBOL_NEGATIVE_SIGN"
    SYMBOL_POSITIVE_SIGN = "SYMBOL_POSITIVE_SIGN"
    SYMBOL_DIGIT = "SYMBOL_DIGIT"
    SYMBOL_OTHER = "SYMBOL_OTHER"

    STATE_INIT = "STATE_INIT"
    STATE_READ_INT = "STATE_READ_INT"
    STATE_READ_IS_OVER = "STATE_READ_IS_OVER"

    def identify_symbol(self, elt) -> string:
        if ord(elt) in range(ord("0"), ord("9") + 1):
            return self.SYMBOL_DIGIT
        elif elt == " ":
            return self.SYMBOL_WHITE_SPACE
        elif elt == "-":
            return self.SYMBOL_NEGATIVE_SIGN
        elif elt == "+":
            return self.SYMBOL_POSITIVE_SIGN
        else:
            return self.SYMBOL_OTHER

    def myAtoi(self, s: str) -> int:
        current_state = self.STATE_INIT
        is_negative = False
        read_digits = ""

        for i in range(0, len(s)):
            if current_state != self.STATE_READ_IS_OVER:
                identified_symbol = self.identify_symbol(s[i])

                if current_state == self.STATE_INIT:
                    if identified_symbol == self.SYMBOL_WHITE_SPACE:
                        pass
                    elif identified_symbol == self.SYMBOL_NEGATIVE_SIGN:
                        is_negative = True
                        current_state = self.STATE_READ_INT
                    elif identified_symbol == self.SYMBOL_POSITIVE_SIGN:
                        current_state = self.STATE_READ_INT
                    elif identified_symbol == self.SYMBOL_DIGIT:
                        current_state = self.STATE_READ_INT
                        read_digits += s[i]
                    elif identified_symbol == self.SYMBOL_OTHER:
                        current_state = self.STATE_READ_IS_OVER

                elif current_state == self.STATE_READ_INT:
                    if identified_symbol == self.SYMBOL_WHITE_SPACE:
                        current_state = self.STATE_READ_IS_OVER
                    elif identified_symbol == self.SYMBOL_NEGATIVE_SIGN:
                        current_state = self.STATE_READ_IS_OVER
                    elif identified_symbol == self.SYMBOL_POSITIVE_SIGN:
                        current_state = self.STATE_READ_IS_OVER
                    elif identified_symbol == self.SYMBOL_DIGIT:
                        read_digits += s[i]
                    elif identified_symbol == self.SYMBOL_OTHER:
                        current_state = self.STATE_READ_IS_OVER

                elif current_state == self.STATE_READ_IS_OVER:
                    pass
        
        if current_state == self.STATE_READ_INT:
            current_state = self.STATE_READ_IS_OVER

        if current_state == self.STATE_READ_IS_OVER:
            if len(read_digits) == 0:
                return 0

            read_digits_as_int = int(read_digits)

            if is_negative:
                read_digits_as_int = read_digits_as_int * -1
                if read_digits_as_int < pow(-2,31):
                    return pow(-2,31)
                else:
                    return read_digits_as_int
            else:
                if read_digits_as_int > pow(2,31) - 1:
                    return pow(2,31) - 1
                else :
                    return read_digits_as_int

        else:
            return 0


solution = Solution()
print(solution.myAtoi("4534783945749357834579345789345"))