function findLHS(nums: number[]): number {
  let longestLength = 0;
  let left = 0,
    right = 0;

  nums.sort((a, b) => a - b);

  while (right < nums.length) {
    if (nums[left] === nums[right]) {
      right++;
    } else if (nums[right] - nums[left] === 1) {
      longestLength = Math.max(longestLength, right - left + 1);
      right++;
    } else {
      left++;
    }
  }

  return longestLength;
}

console.log(findLHS([1, 3, 2, 2, 5, 2, 3, 7]));
