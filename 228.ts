function summaryRanges(nums: number[]): string[] {
  if (nums.length === 0) return [];

  const res: string[] = [];

  let left = 0,
    right = 0;

  while (right + 1 < nums.length) {
    if (nums[right + 1] === nums[right] + 1) {
      right++;
    } else {
      if (right - left !== 0) {
        res.push(`${nums[left]}->${nums[right]}`);
      } else {
        res.push(`${nums[left]}`);
      }
      right++;
      left = right;
    }
  }

  if (right - left !== 0) {
    res.push(`${nums[left]}->${nums[right]}`);
  } else {
    res.push(`${nums[left]}`);
  }

  return res;
}
