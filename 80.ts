function removeDuplicates(nums: (number | null)[]): number {
  if (nums.length < 3) {
    return nums.length;
  }

  let currentValue = nums[0];
  let currentValueCount = 1;
  let writeIndex = 1;

  for (let i = 1; i < nums.length; i++) {
    if (nums[i] === currentValue) {
      currentValueCount++;
    } else {
      currentValueCount = 1;
      currentValue = nums[i];
    }
    if (currentValueCount <= 2) {
      nums[writeIndex++] = nums[i];
    }
  }

  return writeIndex;
}

console.log(removeDuplicates([1, 1, 1, 1]));
