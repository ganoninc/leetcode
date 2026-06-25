from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # best_profit = 0
        # for i in range(0, len(prices)):
        #     current_profit = 0
        #     for j in range(i, len(prices)):
        #         if prices[j] - prices[i] > current_profit:
        #             current_profit = prices[j] - prices[i]
        #     if current_profit > best_profit:
        #         best_profit = current_profit

        best_profit = 0
        smallest_past_min = 100001
        encounted_max_cursor = 0

        for i in range(0, len(prices)):
            if encounted_max_cursor < i:
                encounted_max_cursor = i

            if prices[i] < smallest_past_min:
                smallest_past_min = prices[i]

                if encounted_max_cursor > i:
                    if prices[encounted_max_cursor] - prices[i] > best_profit:
                        best_profit = prices[encounted_max_cursor] - prices[i]
                
                else :
                    for j in range(i+1, len(prices)):
                        if prices[j] > prices[encounted_max_cursor]:
                            encounted_max_cursor = j

                            if prices[j] - prices[i] > best_profit:
                                best_profit = prices[j] - prices[i]

                
        return best_profit

solution = Solution()
print(solution.maxProfit([3,2,6,5,0,3]))
# print(solution.maxProfit([7,1,5,3,6,4]))
# print(solution.maxProfit([7,1,5,3,6,4]))
# print(solution.maxProfit([7,6,4,3,1]))
# print(solution.maxProfit([3,3,5,0,0,3,1,4]))