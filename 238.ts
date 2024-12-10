function productExceptSelf(nums: number[]): number[] {
  let prefixSum = 1,
    sufixSum = 1;
  let prefixSums: number[] = [1];
  let sufixSums: number[] = [1];

  let result: number[] = [];

  for (let i = 0, j = nums.length - 1; i < nums.length; i++, j--) {
    prefixSum = prefixSum * nums[i];
    prefixSums.push(prefixSum);

    sufixSum = sufixSum * nums[j];
    sufixSums.push(sufixSum);
  }

  sufixSums = sufixSums.reverse();

  for (let i = 0; i < nums.length; i++) {
    result.push(prefixSums[i] * sufixSums[i + 1]);
  }

  return result;
}

const nums = [1, 2, 3, 4];
console.log(productExceptSelf(nums));
