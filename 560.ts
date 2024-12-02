function subarraySum(nums: number[], k: number): number {
  if (nums.length == 0) return 0;

  let subarrayCount = 0;
  let prefixSumMap: Map<number, number> = new Map();
  prefixSumMap.set(0, 1);
  let sum = 0;

  for (let i = 0; i < nums.length; i++) {
    sum += nums[i];

    if (prefixSumMap.has(sum - k)) {
      subarrayCount += prefixSumMap.get(sum - k) as number;
    }

    if (!prefixSumMap.get(sum)) prefixSumMap.set(sum, 0);
    prefixSumMap.set(sum, (prefixSumMap.get(sum) as number) + 1);
  }

  return subarrayCount;
}
