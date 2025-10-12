function topKFrequent(nums: number[], k: number): number[] {
  const numFrequencyMap = new Map<number, number>();
  const frequencyBucket: number[][] = Array.from(
    { length: nums.length + 1 },
    () => []
  );
  const res: number[] = [];

  for (let num of nums) {
    numFrequencyMap.set(num, (numFrequencyMap.get(num) || 0) + 1);
  }

  for (let num of numFrequencyMap.keys()) {
    frequencyBucket[numFrequencyMap.get(num) as number].push(num);
  }

  let i = frequencyBucket.length - 1;

  while (i >= 0 && res.length < k) {
    while (frequencyBucket[i].length > 0 && res.length < k) {
      res.push(frequencyBucket[i].pop() as number);
    }
    i--;
  }

  return res;
}
