from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        prev_char = ""
        prev_count = 0
        res = []

        for i in range(0, len(chars)):
            if chars[i] != prev_char:
                if prev_count > 0:
                    self.addCharToCompressedArray(res, prev_char, prev_count)

                prev_char = chars[i]
                prev_count = 1
            else:
                prev_count = prev_count + 1

        self.addCharToCompressedArray(res, prev_char, prev_count)

        for i in range(0, len(res)):
            chars[i] = res[i]

        return len(res)
    
    def addCharToCompressedArray(self, array: List[str], char: str, count: int) -> None:
        array.append(char)
        if count > 1:
            count_as_str = str(count)
            for c in count_as_str:
                array.append(c)

    
sol = Solution()
print(sol.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))