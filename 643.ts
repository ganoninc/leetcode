function findMaxAverage(nums: number[], k: number): number {
  let left = 0,
    right = 0;
  let sum = 0;

  for (; right < k; right++) {
    sum += nums[right];
  }
  let maxSum = sum;

  while (right < nums.length) {
    sum += nums[right];
    sum -= nums[left];
    maxSum = Math.max(maxSum, sum);
    left++;
    right++;
  }

  return maxSum / k;
}

console.log(findMaxAverage([1, 12, -5, -6, 50, 3], 4));
