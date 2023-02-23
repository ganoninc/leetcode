class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        theAlphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        substitutionTable = {
            "a" : None
            , "b" : None
            , "c" : None
            , "d" : None
            , "e" : None
            , "f" : None
            , "g" : None
            , "h" : None
            , "i" : None
            , "j" : None
            , "k" : None
            , "l" : None
            , "m" : None
            , "n" : None
            , "o" : None
            , "p" : None
            , "q" : None
            , "r" : None
            , "s" : None
            , "t" : None
            , "u" : None
            , "v" : None
            , "w" : None
            , "x" : None
            , "y" : None
            , "z" : None
        }

        substitutionTableIndex = 0
        for letter in key:
            if letter!= " " and substitutionTable[letter] == None:
                substitutionTable[letter] = substitutionTableIndex
                substitutionTableIndex += 1

        result = ""
        for letter in message:
            if letter == " ":
                result += " "
            else:
                result += theAlphabet[substitutionTable[letter]]

        return result


solution = Solution()
print(solution.decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv")) #this is a secret