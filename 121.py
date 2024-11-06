from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_buying_price_value = pow(10, 4) + 1
        highest_selling_price_index = 0

        for buying_price_index in range(0, len(prices) - 1):
            if prices[buying_price_index] < lowest_buying_price_value:
                lowest_buying_price_value = prices[buying_price_index]

                if highest_selling_price_index > buying_price_index:
                    current_profit = prices[highest_selling_price_index] - prices[buying_price_index]
                    
                    if current_profit > max_profit:
                        max_profit = current_profit
                else:
                    for selling_price_index in range(buying_price_index + 1, len(prices)):
                        if prices[selling_price_index] > prices[buying_price_index]:
                            if prices[selling_price_index] > prices[highest_selling_price_index]:
                                highest_selling_price_index = selling_price_index

                            current_profit = prices[selling_price_index] - prices[buying_price_index]
                            if current_profit > max_profit:
                                max_profit = current_profit

        return max_profit

solution = Solution()
print(solution.maxProfit([1,2,4]))
# print(solution.maxProfit([7,1,5,3,6,4]))