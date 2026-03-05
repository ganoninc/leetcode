function canBeIncreasing(nums: number[]): boolean {
  let problemCount = 0;

  for (let i = 1; i < nums.length; i++) {
    if (nums[i] <= nums[i - 1]) {
      problemCount++;

      // if nums[i] is bigger than nums[i-2], we keep nums[i] as value because we know at this point it's smaller than nums[i-1],
      // and the smaller the better because it incrases the chances of having something bigger afterward.
      if (i > 1 && nums[i] <= nums[i - 2]) {
        nums[i] = nums[i - 1];
      }
    }

    if (problemCount > 1) return false;
  }

  return true;
}

canBeIncreasing([1, 2, 10, 5, 7]);
