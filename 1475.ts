function finalPrices(prices: number[]): number[] {
  const monotonicStack: number[] = [];
  const res: number[] = [...prices];

  for (let i = prices.length - 1; i >= 0; i--) {
    while (
      monotonicStack.length > 0 &&
      monotonicStack[monotonicStack.length - 1] > prices[i]
    ) {
      monotonicStack.pop();
    }

    if (monotonicStack.length > 0) {
      res[i] = prices[i] - monotonicStack[monotonicStack.length - 1];
    }

    monotonicStack.push(prices[i]);
  }

  return res;
}
