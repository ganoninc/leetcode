function maxProfit(prices: number[]): number {
  let maxProfit = 0;
  let minValue = Infinity;

  for (let i = 0; i < prices.length; i++) {
    minValue = Math.min(minValue, prices[i]);
    maxProfit = Math.max(maxProfit, prices[i] - minValue);
  }

  return maxProfit;
}

console.log(maxProfit([7, 1, 5, 3, 6, 4]));
