function missingNumber(nums: number[]): number {
  nums.sort((a, b) => a - b);

  let left = 0,
    right = nums.length - 1;

  while (left <= right) {
    let mid = left + Math.floor((right - left) / 2);

    if (nums[mid] === mid) left = mid + 1;
    else if (nums[mid] > mid) right = mid - 1;
  }

  return left;
}
