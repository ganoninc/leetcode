class Solution:
    def isSubsequence(self, substrings: list[str], t: str) -> list[bool]:
        letter_index = {}

        for i in range(0, len(t)):
            if t[i] not in letter_index:
                letter_index[t[i]] = []

            letter_index[t[i]].append(i)

        res = [False] * len(substrings)

        for i in range(0, len(substrings)):
            index = -1

            for j in range(0, len(substrings[i])):
                letter = substrings[i][j]

                if letter not in letter_index:
                    break

                index = self.binarySearch(letter_index[letter], index + 1)

                if index == -1:
                    break

                if j == len(substrings[i]) -1:
                    res[i] = True

        return res  
    

    def binarySearch(self, letter_positions: list[int], target: int) -> int:
        left = 0
        right = len(letter_positions) -1
        answer = -1

        while left <= right:
            mid = left + (right - left ) // 2

            if letter_positions[mid] >= target:
                answer = mid
                right = mid -1
            else:
                left = mid + 1
        
        return answer


sol = Solution()
print(sol.isSubsequence(["abc", "ac", "zs", "adab"], "abcdabcdez"))
