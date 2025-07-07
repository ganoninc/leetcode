function maximumPopulation(logs: number[][]): number {
  const yearPopulation: number[] = new Array(101).fill(0);
  for (const log of logs) {
    yearPopulation[log[0] - 1949] += 1;
    yearPopulation[log[1] - 1949] -= 1;
  }

  let sum = 0;
  const prefixSum: number[] = [0];

  for (let i = 0; i < yearPopulation.length; i++) {
    sum += yearPopulation[i];
    prefixSum.push(sum);
  }

  let maxIndex = 0;
  for (let i = 0; i < prefixSum.length; i++) {
    if (prefixSum[i] > prefixSum[maxIndex]) {
      maxIndex = i;
    }
  }

  return maxIndex + 1948;
}
