function largestAltitude(gain: number[]): number {
  let sum: number = 0;
  let highestGain: number = 0;

  for (const g of gain) {
    sum += g;
    highestGain = Math.max(sum, highestGain);
  }

  return highestGain;
}
