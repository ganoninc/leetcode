import string
from typing import Dict


class Solution:

    SYMBOL_LOWERCASE_ENGLISH_LETTER = "SYMBOL_LOWERCASE_ENGLISH_LETTER"
    SYMBOL_ANY_SINGLE_CHARACTER = "SYMBOL_ANY_SINGLE_CHARACTER"
    SYMBOL_ZERO_OR_MORE_REPETITION = "SYMBOL_ZERO_OR_MORE_REPETITION"

    CHECK_REPEATED_ANY_SINGLE_CHARACTER = "CHECK_REPEATED_ANY_SINGLE_CHARACTER"
    CHECK_REPEATED_LOWER_CASE_ENGLISH_LETTER = "CHECK_REPEATED_LOWER_CASE_ENGLISH_LETTER"
    CHECK_UNIQUE_ANY_SINGLE_CHARACTER = "CHECK_UNIQUE_ANY_SINGLE_CHARACTER"
    CHECK_UNIQUE_LOWER_CASE_ENGLISH_LETTER = "CHECK_UNIQUE_LOWER_CASE_ENGLISH_LETTER"

    is_valid = False

    check_chain = []

    check_index = 0

    def identify_symbol(self, elt) -> string:
        if elt == ".":
            return self.SYMBOL_ANY_SINGLE_CHARACTER
        elif elt == "*":
            return self.SYMBOL_ZERO_OR_MORE_REPETITION
        else:
            return self.SYMBOL_LOWERCASE_ENGLISH_LETTER


    def apply_check_unique_any_single_character(self, c:string) -> bool:
        c_symbol_type = self.identify_symbol(c)

        return c_symbol_type == self.SYMBOL_LOWERCASE_ENGLISH_LETTER

    def apply_check_unique_lower_case_english_letter(self, c:string, accepted_lowercase_english_letter:string) -> Dict:
        result_of_check = {
            "is_accepted" : False,
            "is_over" : True
        }

        if c == accepted_lowercase_english_letter:
            result_of_check["is_accepted"] = True
        else:
            result_of_check["is_over"] = True

        return result_of_check


    def apply_check_repeated_any_single_character(self, c:string) -> bool:
        # c_symbol_type = self.identify_symbol(c)
        # return c_symbol_type == self.SYMBOL_LOWERCASE_ENGLISH_LETTER
        return True


        
    def apply_check_repeated_lower_case_english_letter(self, c:string, accepted_lowercase_english_letter:string) -> bool:
        return c == accepted_lowercase_english_letter


    def evaluate_string_using_check_chain(self, s:string) -> bool:
        self.is_valid = False
        check_chain_index = 0
        char_index = 0
        self.evaluate_char_using_check_chain(check_chain_index, char_index, s)
        return self.is_valid

    def evaluate_char_using_check_chain(self, check_chain_index:int, char_index:int, s:string):
        if self.is_valid == False:
            if check_chain_index >= len(self.check_chain) or char_index >= len(s):
                return None

            if check_chain_index == len(self.check_chain) - 1 and char_index == len(s) - 1:
                self.is_valid = True
            else:
                if self.check_chain[check_chain_index]["check_name"] == self.CHECK_REPEATED_ANY_SINGLE_CHARACTER:
                    self.evaluate_char_using_check_chain(check_chain_index, char_index + 1, s)
                    self.evaluate_char_using_check_chain(check_chain_index + 1, char_index + 1, s)
                    self.evaluate_char_using_check_chain(check_chain_index + 1, char_index, s)

                elif self.check_chain[check_chain_index]["check_name"] == self.CHECK_REPEATED_LOWER_CASE_ENGLISH_LETTER:
                    if self.apply_check_repeated_lower_case_english_letter(s[char_index], self.check_chain[check_chain_index]["lower_case_english_letter"]):
                        self.evaluate_char_using_check_chain(check_chain_index, char_index + 1, s)
                        self.evaluate_char_using_check_chain(check_chain_index + 1, char_index + 1, s)
                        self.evaluate_char_using_check_chain(check_chain_index + 1, char_index, s)
                    else:
                        return None

                elif self.check_chain[check_chain_index]["check_name"] == self.CHECK_UNIQUE_ANY_SINGLE_CHARACTER:
                    if self.apply_check_unique_any_single_character(s[char_index]):
                        self.evaluate_char_using_check_chain(check_chain_index + 1, char_index + 1, s)
                    else:
                        return None

                elif self.check_chain[check_chain_index]["check_name"] == self.CHECK_UNIQUE_LOWER_CASE_ENGLISH_LETTER:
                    if self.apply_check_unique_lower_case_english_letter(s[char_index], self.check_chain[check_chain_index]["lower_case_english_letter"]):
                        self.evaluate_char_using_check_chain(check_chain_index + 1, char_index + 1, s)
                    else:
                        return None

    

    def isMatch(self, s: str, p: str) -> bool:
        self.init_check_chain(p)
        print(self.check_chain)
        has_passed_the_check_chain = self.evaluate_string_using_check_chain(s)
        return has_passed_the_check_chain


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
                        "check_name" : self.CHECK_REPEATED_LOWER_CASE_ENGLISH_LETTER,
                        "lower_case_english_letter": previsouly_read_char["value"]
                    })
                elif previsouly_read_char["identified_symbol"] == self.SYMBOL_ANY_SINGLE_CHARACTER:
                    self.check_chain.append({
                        "check_name" : self.CHECK_REPEATED_ANY_SINGLE_CHARACTER,
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
print(solution.isMatch("aba", "abb"))