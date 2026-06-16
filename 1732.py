from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        largest_altitude = 0
        sum = 0
        
        for net_gain in gain:
            sum += net_gain
            largest_altitude = max(largest_altitude, sum)

        return largest_altitude

sol = Solution()
sol.largestAltitude([-4,-3,-2,-1,4,3,2])


