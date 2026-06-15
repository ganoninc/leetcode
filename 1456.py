class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_count = 0

        for i in range(0,k):
            if self.isVowel(s[i]):
                vowel_count += 1

        max_vowels = vowel_count

        i = 1
        j = i + k - 1

        while j < len(s):
            vowel_count -= self.isVowel(s[i-1])
            vowel_count += self.isVowel(s[j])

            max_vowels = max(max_vowels, vowel_count)

            if max_vowels == k:
                return max_vowels

            i += 1
            j += 1

        return max_vowels
    
    def isVowel(self, letter: str) -> bool:
        return letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' 

# s = "abciiidef", k = 3