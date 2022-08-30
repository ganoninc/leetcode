class Solution:
    def climbStairs(self, n: int) -> int:
        return self.solve(n, 0)
    
    @cache
    def solve(self, n: int, current_index:int) -> None:
        if current_index < n:
            return self.solve(n, current_index + 1) + self.solve(n, current_index + 2)
        elif current_index == n:
            return 1
        else:
            return 0


solution = Solution()
print(solution.climbStairs(38))