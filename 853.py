from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        sorted_position_and_speed = sorted(zip(position, speed), reverse=True)

        for p, s in sorted_position_and_speed:
            duration_to_target = (target - p) / s

            stack.append(duration_to_target)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
        return len(stack)
    

solution = Solution()
print(solution.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))