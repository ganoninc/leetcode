function longestConsecutive(nums: number[]): number {
  const set = new Set<number>();
  let longestLength = 0;

  for (let i = 0; i < nums.length; i++) {
    set.add(nums[i]);
  }

  for (const num of set) {
    if (!set.has(num - 1)) {
      let length = 1;
      let j = num;
      while (set.has(j + 1)) {
        length++;
        j++;
      }

      longestLength = Math.max(longestLength, length);
    }
  }

  return longestLength;
}
