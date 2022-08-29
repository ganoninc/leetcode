import math

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        if x == 1:
            return 1

        result = 0
        start = 0
        end = 2147483647
        
        if (start + end) % 2 != 0:
            end = end + 1
        m = start + end / 2

        is_not_over = True

        while is_not_over:
            if m * m > x and end - start > 1:
                end = m - 1
            
            elif m * m < x and end - start > 1:
                start = m 

            elif m * m == x:
                result = m
                is_not_over = False
            else:    
                result = end
                is_not_over = False

            if (start + end) % 2 != 0:
                end = end + 1
            m = (start + end) / 2

        return math.floor(result)
        

solution = Solution()
print(solution.mySqrt(2))