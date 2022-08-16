from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        similar_char_occurences = {}
        j = 0
        for firstWordCharIndex in range(0, len(strs[0])):
            similar_char_occurences[firstWordCharIndex] = 0;
            for i in range(1, len(strs)):
                if (firstWordCharIndex < len(strs[i])) and (strs[0][firstWordCharIndex] == strs[i][firstWordCharIndex]):
                    similar_char_occurences[firstWordCharIndex] += 1
            if similar_char_occurences[firstWordCharIndex] == (len(strs) - 1):
                result += strs[0][firstWordCharIndex]
            else:
                break

        return result
        

print(Solution.longestCommonPrefix(Solution, ["flower","flow","flight"]))
print(Solution.longestCommonPrefix(Solution, ["dog","racecar","car"]))
print(Solution.longestCommonPrefix(Solution, ["ab", "a"]))
