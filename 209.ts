function minSubArrayLen(target: number, nums: number[]): number {
  let prefixSums: number[] = [0];
  let sum = 0;
  let shortestSubArray = 0;

  for (let i = 0; i < nums.length; i++) {
    sum += nums[i];
    prefixSums.push(sum);

    if (nums[i] >= target) {
      shortestSubArray = 1;
      return shortestSubArray;
    }

    let shortestSubarryForIHasBeenFound = false;
    for (let j = i; j >= 0 && !shortestSubarryForIHasBeenFound; j--) {
      let sumTarget = sum - target;
      if (prefixSums[j] <= sumTarget) {
        let subarraySum = sum - prefixSums[j];

        if (
          (subarraySum >= target && i - j + 1 < shortestSubArray) ||
          (subarraySum >= target && shortestSubArray === 0)
        ) {
          shortestSubArray = i - j + 1;

          if (shortestSubArray === 1) return shortestSubArray;

          shortestSubarryForIHasBeenFound = true;
        }
      }
    }
  }

  return shortestSubArray;
}

const testArray = [2, 3, 1, 2, 4, 3];
console.log(minSubArrayLen(7, testArray));
