from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        going_right = []
        going_left = []

        for asteroid in asteroids:
            if asteroid > 0:
                going_right.append(asteroid)
            else:
                while len(going_right) > 0 and going_right[-1] < abs(asteroid):
                    going_right.pop()

                if len(going_right) > 0 and going_right[-1] == abs(asteroid):
                    going_right.pop()
                elif len(going_right) == 0:
                    going_left.append(asteroid)

        return going_left + going_right
    