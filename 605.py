from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        decorated_flowerbed = [0] + flowerbed + [0]

        empty_pot_count = 0
        max_available_pot_count = 0

        for emplacement in decorated_flowerbed:
            if emplacement == 0:
                empty_pot_count += 1

            elif empty_pot_count > 0: 
                max_available_pot_count += self.getActuallyAvailablePotCount(empty_pot_count)
                empty_pot_count = 0

        max_available_pot_count += self.getActuallyAvailablePotCount(empty_pot_count)

        return n <= max_available_pot_count
    
    def getActuallyAvailablePotCount(self, empty_pot_count : int) -> int:
        closest_odd_number = empty_pot_count

        if empty_pot_count % 2 == 0:
            closest_odd_number = empty_pot_count - 1

        return closest_odd_number // 2

    
sol = Solution()
print(sol.canPlaceFlowers([1,0,0,0,1,0,0], 2))
print(sol.canPlaceFlowers([0,0,1,0,1], 1))
print(sol.canPlaceFlowers([1,0,0,0,1], 1))
print(sol.canPlaceFlowers([1,0,0,0,0,1], 2))