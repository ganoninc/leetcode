import string


class Solution:

    SYMBOL_LOWERCASE_ENGLISH_LETTER = "SYMBOL_LOWERCASE_ENGLISH_LETTER"
    SYMBOL_ANY_SINGLE_CHARACTER = "SYMBOL_ANY_SINGLE_CHARACTER"
    SYMBOL_ZERO_OR_MORE_REPETITION = "SYMBOL_ZERO_OR_MORE_REPETITION"

    CHECK_REPEATED_ANY_SINGLE_CHARACTER = "CHECK_REPEATED_ANY_SINGLE_CHARACTER"
    CHECK_REPEATED_LOWER_CASE_ENGLISH_LETTER = "CHECK_REPEATED_LOWER_CASE_ENGLISH_LETTER"
    CHECK_UNIQUE_ANY_SINGLE_CHARACTER = "CHECK_UNIQUE_ANY_SINGLE_CHARACTER"
    CHECK_UNIQUE_LOWER_CASE_ENGLISH_LETTER = "CHECK_UNIQUE_LOWER_CASE_ENGLISH_LETTER"

    check_chain = []

    def identify_symbol(self, elt) -> string:
        if elt == ".":
            return self.SYMBOL_ANY_SINGLE_CHARACTER
        elif elt == "*":
            return self.SYMBOL_ZERO_OR_MORE_REPETITION
        else:
            return self.SYMBOL_LOWERCASE_ENGLISH_LETTER

    def isMatch(self, s: str, p: str) -> bool:
        self.init_check_chain(p)
        print(self.check_chain)
        return False

    def init_check_chain(self, p:str) -> None:
        previsouly_read_char = {
            "identified_symbol" :None,
            "value" : "",
        }

        for i in range(0, len(p)):
            identified_symbol = self.identify_symbol(p[i])

            if identified_symbol == self.SYMBOL_ZERO_OR_MORE_REPETITION:
                if previsouly_read_char["identified_symbol"] == self.SYMBOL_LOWERCASE_ENGLISH_LETTER:
                    self.check_chain.append({
                        "check_name" : self.CHECK_REPEATED_ANY_SINGLE_CHARACTER,
                    })
                elif previsouly_read_char["identified_symbol"] == self.SYMBOL_ANY_SINGLE_CHARACTER:
                    self.check_chain.append({
                        "check_name" : self.CHECK_REPEATED_LOWER_CASE_ENGLISH_LETTER,
                        "lower_case_english_letter": previsouly_read_char["value"]
                    })
            elif identified_symbol == self.SYMBOL_ANY_SINGLE_CHARACTER:
                if previsouly_read_char["identified_symbol"] == self.SYMBOL_LOWERCASE_ENGLISH_LETTER:
                    self.check_chain.append({
                        "check_name" : self.CHECK_UNIQUE_LOWER_CASE_ENGLISH_LETTER,
                        "lower_case_english_letter": previsouly_read_char["value"]
                    })
                elif previsouly_read_char["identified_symbol"] == self.SYMBOL_ANY_SINGLE_CHARACTER:
                    self.check_chain.append({
                        "check_name" : self.CHECK_UNIQUE_ANY_SINGLE_CHARACTER,
                    })
            elif identified_symbol == self.SYMBOL_LOWERCASE_ENGLISH_LETTER:
                if previsouly_read_char["identified_symbol"] == self.SYMBOL_LOWERCASE_ENGLISH_LETTER:
                    self.check_chain.append({
                        "check_name" : self.CHECK_UNIQUE_LOWER_CASE_ENGLISH_LETTER,
                        "lower_case_english_letter": previsouly_read_char["value"]
                    })
                elif previsouly_read_char["identified_symbol"] == self.SYMBOL_ANY_SINGLE_CHARACTER:
                    self.check_chain.append({
                        "check_name" : self.CHECK_UNIQUE_ANY_SINGLE_CHARACTER,
                    })
            
            previsouly_read_char["value"] = p[i]
            previsouly_read_char["identified_symbol"] = identified_symbol
        
        if previsouly_read_char["identified_symbol"] == self.SYMBOL_ANY_SINGLE_CHARACTER:
            self.check_chain.append({
                "check_name" : self.CHECK_UNIQUE_ANY_SINGLE_CHARACTER,
            })
        elif previsouly_read_char["identified_symbol"] == self.SYMBOL_LOWERCASE_ENGLISH_LETTER:
            self.check_chain.append({
                "check_name" : self.CHECK_UNIQUE_LOWER_CASE_ENGLISH_LETTER,
                "lower_case_english_letter": previsouly_read_char["value"]
            })

solution = Solution()
print(solution.isMatch("aaa", "a*.bc"))