function coinChange(coins: number[], amount: number): number {
  const optimalChanges = new Array(amount + 1);
  optimalChanges[0] = 0;

  for (let i = 1; i <= amount; i++) {
    let coinsCount = Infinity;

    for (let j = 0; j < coins.length; j++) {
      if (coins[j] <= i) {
        let neededComplement = i - coins[j];

        coinsCount = Math.min(coinsCount, optimalChanges[neededComplement] + 1);
      }
    }
    optimalChanges[i] = coinsCount;
  }

  return optimalChanges[amount] === Infinity ? -1 : optimalChanges[amount];
}

console.log(coinChange([1, 2, 5], 11));
