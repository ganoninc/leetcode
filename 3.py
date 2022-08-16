class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substring_length = 0
        # max_substring_index = 0

        for i in range(0, len(s)):
            detected_letters = []
            detected_letters.append(s[i])
            longest_substring_length = 1

            for j in range(i+1, len(s)):

                if j < len(s):
                    if(s[j] not in detected_letters):
                        detected_letters.append(s[j])
                        longest_substring_length = longest_substring_length + 1
                    else:
                        break

            if longest_substring_length > max_substring_length:
                max_substring_length = longest_substring_length
                # max_substring_index = i

        return max_substring_length
        

solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))